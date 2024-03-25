from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Poem(models.Model):
    title = models.CharField(max_length=100)
    content = CKEditor5Field('Text', config_name='extends')
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    date_published = models.DateField(default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.CharField(max_length=100, default="The Dickinsonian Museum staff")

    def __str__(self):
        return self.title