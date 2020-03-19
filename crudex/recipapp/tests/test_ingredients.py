from django.test import TestCase

from recipapp.models import Ingredient
from recipapp.serializers import IngredientSerializer


class IngredientTests(TestCase):
    """
    Test the ingredients model and serializer
    """

    def test_basic_model(self):
        """Test basic functionality for the model and the serializer"""

        # Test model
        Ingredient.objects.create(name='Salt')
        Ingredient.objects.create(name='Sugar')

        ingredients = Ingredient.objects.all().order_by('-name')

        self.assertEqual(len(ingredients), 2)
        self.assertEqual(ingredients[0].name, 'Sugar')
        self.assertEqual(ingredients[1].name, 'Salt')

        # Test serializer
        serializer = IngredientSerializer(ingredients, many=True)
        for i in [0, 1]:
            self.assertEqual(ingredients[i].name, serializer.data[i]['name'])
