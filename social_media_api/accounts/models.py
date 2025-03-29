from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

# Create your models here.
class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='following')

    groups = models.ManyToManyField(Group, related_name='accounts_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='accounts_user_permissions')

