from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title
