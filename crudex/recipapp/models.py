from django.db import models

class Recipe(models.Model):
    """A representation of a recipe"""

    name = models.CharField(max_length=150)
    # description = models.CharField(max_length=255, blank=True, default='')
    description = models.CharField(max_length=255)
    # ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.name

"""
    After having the model Recipe with 'ingredients = models.ManyToManyField('Ingredient')',
    switched to be the model Ingredient who points to recipes, and then the migration
    requires a default recipe id to fill the existing DB values:
"""
DEFAULT_RECIPE_ID = 1

class Ingredient(models.Model):
    """A representation of an ingredient"""

    name = models.CharField(max_length=80)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )

    # class Meta:
    #     ordering = ['name']

    def __str__(self):
        return self.name
