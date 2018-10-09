from django.db import models


class Image(models.Model):
    
    name = models.CharField(
        max_length=250,
        unique=True
    )

    value = models.ImageField()

    def __str__(self):
        return self.name
