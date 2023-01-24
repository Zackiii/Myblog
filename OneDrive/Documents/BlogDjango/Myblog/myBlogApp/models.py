from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', default='image vide')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def image_preview(self):  # new
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')
# Create your models here.
