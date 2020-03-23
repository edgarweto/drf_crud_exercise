from rest_framework import serializers
from recipapp.models import Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """Serialization of ingredient model"""

    class Meta:
        model = Ingredient
        fields = ['name']
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    """Serialization of a recipe model"""

    # ingredients = IngredientSerializer(many=True, read_only=True)
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'ingredients']
        read_only_fields = ('id',)


    def create(self, validated_data):
        """Create a recipe and the ingredients"""
        # print('\n >>>>>>>>>> CREATE!')
        # print(' > validated_data')
        # print(validated_data)

        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingr_data in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingr_data)

        return recipe


class RecipeDetailSerializer(RecipeSerializer):
    """Recover also ingredient models"""

    ingredients = IngredientSerializer(many=True, read_only=True)
