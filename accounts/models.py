from django.db import models

from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):

    image = models.ImageField(
        upload_to='avatars/'
    )

    phone = models.CharField(
        max_length=11,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username


