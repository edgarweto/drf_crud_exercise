from django.test import TestCase
from django.urls import reverse

import json

from rest_framework import status
from rest_framework.test import APIClient

from recipapp.models import Recipe, Ingredient

# Constants and definitions
ENDPOINT_RECIPES = reverse('recipapp:recipe-list')

# Helpers
def new_recipe():
    recipe = Recipe.objects.create(
        name='Another recipe',
        description='This is a dummy recipe')

    return recipe

def add_ingredients(recipe, ingrNames):
    """
    Adds ingredients to the recipe
    """
    for ingrName in ingrNames:
        Ingredient.objects.create(name=ingrName, recipe_id=recipe.id)


class TestRecipesApi(TestCase):
    """
    Test endpoints for Recipes CRUD API
    """

    def setUp(self):
        self.client = APIClient()

    def test_recipes_list(self):
        """Test the GET list for recipes"""

        # Create some recipes
        new_recipe()
        new_recipe()

        result = self.client.get(ENDPOINT_RECIPES)

        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result.data), 2)
        self.assertEqual(result.data[0]['name'], 'Another recipe')

    def test_recipe_detail(self):
        """Test the GET detail of a recipe"""

        # Create a recipe with ingredients
        recipe = new_recipe()
        add_ingredients(recipe, ['sugar', 'salt'])

        detail_url = reverse('recipapp:recipe-detail', args=[recipe.id])

        result = self.client.get(detail_url)

        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['name'], 'Another recipe')
        self.assertEqual(len(result.data['ingredients']), 2)

    def test_recipe_add_with_ingredients(self):
        """Test endpoint for adding recipe with ingredients"""
        payload = {
            'name': 'Soup',
            'description': 'Added from post!',
            'ingredients': [
                { 'name': 'salt' },
                { 'name': 'sugar' }
            ]
        }

        result = self.client.post(ENDPOINT_RECIPES,
                                    json.dumps(payload),
                                    content_type="application/json")

        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.data['name'], 'Soup')
        self.assertEqual(result.data['description'], 'Added from post!')

        # print('\n >>>>> data')
        # print(result.data)

        self.assertEqual(len(result.data['ingredients']), 2)
        self.assertEqual(result.data['ingredients'][0]['name'], 'salt')
        self.assertEqual(result.data['ingredients'][1]['name'], 'sugar')
