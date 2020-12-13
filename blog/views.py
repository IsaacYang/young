from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.views.generic import ListView, DetailView 
from .models import Post
import markdown


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    # 将markdown语法渲染成html样式
    post.body = markdown.markdown(post.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])
    context = { 'post': post }
    return render(request, 'blog/post_detail.html', context)