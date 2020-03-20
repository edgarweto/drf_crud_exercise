from django.test import TestCase
from django.urls import reverse

from recipapp.models import Recipe, Ingredient

# Constants and definitions
ENDPOINT_RECIPES = reverse('recipapp:recipe-list')

# Helpers
def new_recipe():
    recipe = Recipe.objects.create(
        name='Another recipe',
        description='This is a dummy recipe')

    return recipe


class TestRecipesApi(TestCase):
    """
    Test endpoints for Recipes CRUD API
    """

    def test_recipes_list(self):
        """Test the GET list for recipes"""

        # Create some recipes
        new_recipe()
        new_recipe()

        print('\n >>>> ENDPOINT_RECIPES = ' + ENDPOINT_RECIPES)