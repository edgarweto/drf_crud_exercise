from django.db import models

class Recipe(models.Model):
    """A representation of a recipe"""

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.name
