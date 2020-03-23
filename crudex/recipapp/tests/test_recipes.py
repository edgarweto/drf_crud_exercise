from django.test import TestCase

from recipapp.models import Recipe, Ingredient
from recipapp.serializers import RecipeSerializer, RecipeDetailSerializer

def _new_ingredient(name, recipe_id):
    return Ingredient.objects.create(name=name, recipe_id=recipe_id)

def _sample_recipe(ingredientList):
    recipe = Recipe.objects.create(
        name='Capresse Salad',
        description='Best tomato salad'
    )

    for ingrName in ingredientList:
        recipe.ingredients.add(_new_ingredient(ingrName, recipe.id))

    return recipe


class RecipeTests(TestCase):
    """
    Set of tests for recipes
    """

    def test_model(self):
        """Test the model structure"""

        ingredientList = ['tomatoes', 'salt', 'olive oil', 'mozzarella', 'basil', 'iberian ham']
        recipe = _sample_recipe(ingredientList)

        recipes = Recipe.objects.all()

        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0].name, 'Capresse Salad')
        self.assertEqual(recipes[0].description, 'Best tomato salad')

    def test_serializers(self):
        """Test model serializers"""

        ingredientList = ['tomatoes', 'salt', 'olive oil', 'mozzarella', 'basil', 'iberian ham']
        recipe = _sample_recipe(ingredientList)

        serializer = RecipeSerializer(recipe)
        self.assertEqual(len(serializer.data['ingredients']), 6)

        serializer2 = RecipeDetailSerializer(recipe)
        self.assertEqual(len(serializer2.data['ingredients']), 6)

        for i in range(len(ingredientList)):
            self.assertEqual(serializer2.data['ingredients'][i]['name'], ingredientList[i])
