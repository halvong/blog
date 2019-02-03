from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


