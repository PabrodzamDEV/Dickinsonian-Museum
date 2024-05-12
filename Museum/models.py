import os

from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User


class Poem(models.Model):
    CATEGORY_CHOICES = [
        ('nature', 'Nature'),
        ('love', 'Love'),
        ('life', 'Life'),
        ('death', 'Death'),
        ('reflection', 'Reflection'),
    ]

    LANGUAGE_CHOICES = [
        ('ENG', 'English'),
        ('FR', 'French'),
        ('SPA', 'Spanish'),
    ]

    title = models.CharField(max_length=100)
    content = CKEditor5Field('Text', config_name='extends')
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='nature')
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default='ENG')
    date_published = models.DateField(default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class GalleryPiece(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery_images')
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


def essay_file_path(instance, filename, title):
    # Get timestamp for the present moment
    now = timezone.localtime()
    # Get the file extension
    _, ext = os.path.splitext(filename)
    # Generate a unique filename based on the user's ID
    filename = f"user_{instance.user.id}_essay_{title}_{now}{ext}"
    # File will be uploaded to MEDIA_ROOT/essays/user_<id>/user_<id>_essay_{title}_{now}.<ext>
    return os.path.join("essays", f"user_{instance.user.id}", filename)


class Essay(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to=essay_file_path, blank=True)
    is_academic = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
