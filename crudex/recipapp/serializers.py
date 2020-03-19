from rest_framework import serializers
from recipapp.models import Recipe, Ingredient


class RecipeSerializer(serializers.ModelSerializer):
    """Serialization of a recipe model"""

    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('name', 'description', 'ingredients')
        read_only_fields = ('id',)

    def create(self, validated_data):
        """Create and return a new Recipe instance from the validated data"""
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing Recipe instance using the validated data"""

        instance.description = instance.description + ' (Edited)'
        instance.save()
        return instance


class IngredientSerializer(serializers.ModelSerializer):
    """Serialization of ingredient model"""

    class Meta:
        model = Ingredient
        fields = ('name',)
        read_only_fields = ('id',)


class RecipeDetailSerializer(RecipeSerializer):
    """Recover also ingredient models"""

    ingredients = IngredientSerializer(many=True, read_only=True)
