from django.db import models

class Recipe(models.Model):
    """A representation of a recipe"""

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255, blank=True, default='')
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """A representation of an ingredient"""

    name = models.CharField(max_length=80)
    # recipe = models.ForeignKey(
    #     Recipe,
    #     on_delete=models.CASCADE
    # )

    def __str__(self):
        return self.name
