from django.db import models
from django.contrib.auth.models import User
import datetime

STATUS = (
    (0,'Draft'),
    (1,'Publish')
)

# Create your models here.
class Post(models.Model):
    """Model definition for Post."""

    # TODO: Define fields here
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField( max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS,default=0)

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-created',)

    def __str__(self):
        """Unicode representation of Post."""
        return self.title
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blog:index.html', kwargs={'pk': self.pk})

class Comment(models.Model):
    """Model definition for Comment."""

    # TODO: Define fields here
    post = models.ManyToManyField(Post)
    comments = models.ManyToManyField('Comment', null=True, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,null=True,blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created',)

    def __str__(self):
        """Unicode representation of Comment."""
        return self.name+'says: '+self.body+"on "+ datetime.datetime.strftime(self.created,'%Y-%m-%d')
