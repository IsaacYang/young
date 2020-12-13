from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('title','author', 'created','updated','status')
    list_filter = ('status','created')
    search_fields = ('title','body')
    ordering = ('-created',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Admin View for Comment'''

    list_display = ('name','email','body','created',)
    list_filter = ('active','created')
    search_fields = ('name','body','email')
    ordering = ('-created',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
