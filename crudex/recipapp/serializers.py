from rest_framework import serializers
from recipapp.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serialization of a recipe model"""

    class Meta:
        model = Recipe
        fields = ('name', 'description')
        read_only_fields = ('id',)

    def create(self, validated_data):
        """Create and return a new Recipe instance from the validated data"""
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing Recipe instance using the validated data"""

        instance.description = instance.description + ' (Edited)'
        instance.save()
        return instance