import base64
import io
import os

from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User

from pdf2image import convert_from_path


class Poem(models.Model):
    CATEGORY_CHOICES = [
        ('nature', 'Nature'),
        ('love', 'Love'),
        ('life', 'Life'),
        ('death', 'Death'),
        ('reflection', 'Reflection'),
        ('other', 'Other'),
    ]

    LANGUAGE_CHOICES = [
        ('ENG', 'English'),
        ('FR', 'French'),
        ('SPA', 'Spanish'),
        ('OTH', 'Other'),
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


def gallery_file_path(instance, filename):
    # Get timestamp for the present moment
    now = timezone.localtime()
    # Get the file extension
    _, ext = os.path.splitext(filename)
    # Generate a unique filename based on the user's ID
    filename = f"user_{instance.user.id}_piece_{instance.title}_{now}{ext}"
    # File will be uploaded to MEDIA_ROOT/essays/user_<id>/user_<id>_essay_{title}_{now}.<ext>
    return os.path.join("gallery_pieces", f"user_{instance.user.id}", filename)


class GalleryPiece(models.Model):
    CATEGORY_CHOICES = [
        ('photograph', 'Photograph'),
        ('painting', 'Painting'),
        ('drawing', 'Drawing'),
        ('video', 'Video'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=100)
    piece = models.FileField(upload_to=gallery_file_path)
    author = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='other')
    date_published = models.DateField(default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def file_type(self):
        _, ext = os.path.splitext(self.piece.name)
        if ext.lower() in ['.jpg', '.png', '.gif']:
            return 'image'
        elif ext.lower() in ['.webm', '.mp4']:
            return 'video'
        else:
            return 'unknown'

    def __str__(self):
        return self.title


# Function that determines the filepath for every essay uploaded
def essay_file_path(instance, filename):
    # Get timestamp for the present moment
    now = timezone.localtime()
    # Get the file extension
    _, ext = os.path.splitext(filename)
    # Generate a unique filename based on the user's ID
    filename = f"user_{instance.user.id}_essay_{instance.title}_{now}{ext}"
    # File will be uploaded to MEDIA_ROOT/essays/user_<id>/user_<id>_essay_{title}_{now}.<ext>
    return os.path.join("essays", f"user_{instance.user.id}", filename)


class Essay(models.Model):
    CATEGORY_CHOICES = [
        ('literary', 'Literary'),
        ('philosophical', 'Philosophical'),
        ('aesthetic theory', 'Aesthetic Theory'),
        ('pictorial', 'Pictorial'),
        ('photographic', 'Photographic'),
        ('sculptural', 'Sculptural'),
        ('architectural', 'Architectural'),
        ('other', 'Other'),
    ]

    LANGUAGE_CHOICES = [
        ('ENG', 'English'),
        ('FR', 'French'),
        ('SPA', 'Spanish'),
        ('OTH', 'Other'),
    ]

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    file = models.FileField(upload_to=essay_file_path)
    is_academic = models.BooleanField(default=False)
    abstract = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Aesthetic Theory')
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default='ENG')
    date_published = models.DateField(default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def file_type(self):
        _, ext = os.path.splitext(self.file.name)
        if ext.lower() in ['.pdf']:
            return 'pdf'
        elif ext.lower() in ['.jpg', '.png', '.gif']:
            return 'image'
        elif ext.lower() in ['.webm', '.mp4']:
            return 'video'
        else:
            return 'unknown'

    # Returns the pdf cover as a base64 string in order to display it on a template
    def get_pdf_cover(self):
        if self.file:
            images = convert_from_path(self.file.path, first_page=1, last_page=1,
                                       poppler_path=r"C:\Users\pablo\Downloads\poppler-24.02.0\Library\bin")
            # Convert the first page to an image
            image = images[0]

            # Save the image to a BytesIO object
            image_bytes = io.BytesIO()
            image.save(image_bytes, format='PNG')

            # Get the base64 encoded string
            image_base64 = base64.b64encode(image_bytes.getvalue()).decode('utf-8')

            return image_base64

    def __str__(self):
        return self.title
