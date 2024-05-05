import os

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.http import urlencode


def profile_image_path(instance, filename):
    # Get the file extension
    _, ext = os.path.splitext(filename)
    # Generate a unique filename based on the user's ID
    filename = f"user_{instance.user.id}_profpic{ext}"
    # File will be uploaded to MEDIA_ROOT/profile_images/user_<id>/user_<id>_profpic.<ext>
    return os.path.join("profile_images", f"user_{instance.user.id}", filename)


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to=profile_image_path, blank=True, default='/profile_images/default.png')
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    # Generates an url with a timestamp as a query parameter so that the image never gets cached.
    # This prevents the undesired behaviour that browsers will store a local copy of the profile
    # picture, preventing the user from seeing their new picture if they were to update it.
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            url = self.avatar.url
            time = timezone.localtime().isoformat()
            return url + "?" + urlencode({'t': time})
        return None

    def delete_old_avatar(self):
        # Delete the old avatar file if it exists and is not the default one
        if self.avatar and 'default.png' not in self.avatar.name:
            try:
                os.remove(self.avatar.path)
            except FileNotFoundError:
                pass

    def save(self, *args, **kwargs):
        # Delete old avatar before saving new one if avatar field has changed
        if self.pk:  # Check if instance already exists
            orig = Profile.objects.get(pk=self.pk)
            if orig.avatar != self.avatar:
                orig.delete_old_avatar()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Clear or reset fields instead of deleting the profile object
        self.bio = ""
        self.avatar = '/profile_images/default.png'
        self.location = ""
        self.birth_date = None
        self.save()

    def __str__(self):
        return f"{self.user.username}'s Profile"
