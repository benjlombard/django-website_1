from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

from .elastic_search_connection import PostsIndex

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')



class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now = True)
    publish = models.DateTimeField(default = timezone.now)
    status = models.CharField(max_length=10,choices = STATUS_CHOICES,default='draft')

    #objects = models.Manager()
    published = PublishedManager()

    # indexing method of Question model
    def indexing(self):
        obj = PostsIndex(
            meta={
                'id': self.id
            },
            author=self.author,
            publish=self.publish,
            body=self.body
        )
        obj.save()
        return obj.to_dict(include_meta=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.publish.year,self.publish.month,self.publish.day,self.slug])
