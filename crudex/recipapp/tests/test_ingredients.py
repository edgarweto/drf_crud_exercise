from django.test import TestCase

from recipapp.models import Ingredient, Recipe
from recipapp.serializers import IngredientSerializer


class IngredientTests(TestCase):
    """
    Test the ingredients model and serializer
    """

    def setUp(self):
        """
        Trying to avoid 'django.db.utils.IntegrityError: NOT NULL constraint failed: recipapp_ingredient.recipe_id'
        """
        recipe = Recipe.objects.create(
            name='FIRST recipe',
            description='Trying to fix NOT NULL constraint failed: recipapp_ingredient.recipe_id')

        self.recipe = recipe


    def test_basic_model(self):
        """Test basic functionality for the model and the serializer"""

        # Test model
        recipe_id = self.recipe.id
        Ingredient.objects.create(name='Salt', recipe_id=recipe_id)
        Ingredient.objects.create(name='Sugar', recipe_id=recipe_id)

        ingredients = Ingredient.objects.all().order_by('-name')

        self.assertEqual(len(ingredients), 2)
        self.assertEqual(ingredients[0].name, 'Sugar')
        self.assertEqual(ingredients[1].name, 'Salt')

        # Test serializer
        serializer = IngredientSerializer(ingredients, many=True)
        for i in [0, 1]:
            self.assertEqual(ingredients[i].name, serializer.data[i]['name'])
