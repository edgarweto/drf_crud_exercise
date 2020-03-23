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
        fields = ['id', 'name', 'description', 'ingredients']
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

    def update(self, instance, validated_data):
        """Updates a recipe instance"""
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)

        ingredients_data = validated_data.pop('ingredients')

        new_ingredient_names = [ingr['name'] for ingr in ingredients_data]

        # First, remove unused ingredients
        current_ingredients = instance.ingredients.all()
        for ingr_data in current_ingredients:
            name = ingr_data.name
            if not name in new_ingredient_names:
                Ingredient.objects.filter(id=ingr_data.id).delete()

        current_ingredient_names = [ingr.name for ingr in current_ingredients]

        # Now add the new ones
        for ingr_data in ingredients_data:
            name = ingr_data['name']
            if not name in current_ingredient_names:
                Ingredient.objects.create(recipe=instance, **ingr_data)

        return instance


class RecipeDetailSerializer(RecipeSerializer):
    """Recover also ingredient models"""

    ingredients = IngredientSerializer(many=True, read_only=True)
