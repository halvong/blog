from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import  TaggableManager

class PublishedManager(models.Manager):
    '''
    SELECT "blogi_post"."id", "blogi_post"."title", "blogi_post"."slug", "blogi_post"."author_id",
    "blogi_post"."body", "blogi_post"."publish", "blogi_post"."created", "blogi_post"."updated", "blogi_post"."status"
    FROM "blogi_post" WHERE ("blogi_post"."status" = 'published'
    AND "blogi_post"."title"::text LIKE Who%) ORDER BY "blogi_post"."publish" DESC'
    '''
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):

    tags = TaggableManager()

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    def get_absolute_url(self):
        return reverse('blogi:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')#associate comment with a single post.
                                                                                     #a post have many comments
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
