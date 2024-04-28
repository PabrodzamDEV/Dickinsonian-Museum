from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User  # Django's built-in User model


# Create your models here.
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
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
