from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    biography = models.TextField(blank=True)
    birth_date = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.user.username