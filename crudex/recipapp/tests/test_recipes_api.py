from django.test import TestCase
from django.urls import reverse

import json

from rest_framework import status
from rest_framework.test import APIClient

from recipapp.models import Recipe, Ingredient

# Constants and definitions
ENDPOINT_RECIPES = reverse('recipapp:recipe-list')

# Helpers
def new_recipe(name=''):
    recipe = Recipe.objects.create(
        name = name or 'Another recipe',
        description = 'This is a dummy recipe')

    return recipe

def add_ingredients(recipe, ingrNames):
    """Adds ingredients to the recipe"""
    for ingrName in ingrNames:
        Ingredient.objects.create(name=ingrName, recipe_id=recipe.id)

def recipe_detail_url(recipe_id):
    """Return recipe detail URL"""
    return reverse('recipapp:recipe-detail', args=[recipe_id])


class TestRecipesApi(TestCase):
    """Test endpoints for Recipes CRUD API"""

    def setUp(self):
        self.client = APIClient()

    def test_recipes_list(self):
        """Test the GET list for recipes"""

        # Create some recipes
        new_recipe()
        recipe = new_recipe()
        add_ingredients(recipe, ['sugar', 'salt'])

        result = self.client.get(ENDPOINT_RECIPES)

        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result.data), 2)
        self.assertEqual(result.data[0]['name'], 'Another recipe')

        ingr_list_1 = result.data[0]['ingredients']
        self.assertEqual(len(ingr_list_1), 0)

        ingr_list_2 = result.data[1]['ingredients']
        self.assertEqual(len(ingr_list_2), 2)
        self.assertEqual(ingr_list_2[0]['name'], 'sugar')

    def test_recipes_list_search(self):
        """Test list-search functionality for recipes"""

        # Create some recipes
        new_recipe('pizza')
        recipe = new_recipe('gazpacho')
        add_ingredients(recipe, ['sugar', 'salt'])

        result = self.client.get(ENDPOINT_RECIPES, {'name':'gazpacho'})

        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result.data), 1)
        self.assertEqual(result.data[0]['name'], 'gazpacho')
        self.assertEqual(result.data[0]['ingredients'][0]['name'], 'sugar')

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
        self.assertEqual(result.data['ingredients'][0]['name'], 'sugar')

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
        self.assertEqual(len(result.data['ingredients']), 2)
        self.assertEqual(result.data['ingredients'][0]['name'], 'salt')
        self.assertEqual(result.data['ingredients'][1]['name'], 'sugar')

    def test_recipe_edit(self):
        """Test endpoint for editing ingredients of a recipe"""

        # Create a recipe with ingredients
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

        # Now edit the description and the ingredient list
        recipe_id = result.data['id']

        payload2 = {
            'name': payload['name'],
            'description': 'Boil it 5 min',
            'ingredients': [
                { 'name': 'water' }
            ]
        }

        edited = self.client.patch(recipe_detail_url(recipe_id),
                                    json.dumps(payload2),
                                    content_type="application/json")

        self.assertEqual(edited.data['description'], 'Boil it 5 min')
        self.assertEqual(len(edited.data['ingredients']), 1)
        self.assertEqual(edited.data['ingredients'][0]['name'], 'water')

    def test_recipe_delete(self):
        """Test endpoint for editing ingredients of a recipe"""

        # Create a recipe with ingredients
        recipe = new_recipe('to_be_deleted_recipe')
        add_ingredients(recipe, ['sugar-123', 'salt-123'])

        # Delete the recipe (and the ingredients)
        delete_url = reverse('recipapp:recipe-detail', args=[recipe.id])
        result = self.client.delete(delete_url)
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)

        # Now check that the recipe is not there:
        result = self.client.get(ENDPOINT_RECIPES, {'name':'to_be_deleted_recipe'})
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result.data), 0)

        # Check that ingredients have been deleted as well
        all_ingr_names = [ingr.name for ingr in Ingredient.objects.all()]
        self.assertEqual(len(all_ingr_names), 0)
