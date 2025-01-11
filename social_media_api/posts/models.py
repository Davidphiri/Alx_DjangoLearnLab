from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add fields for your custom user model here
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
