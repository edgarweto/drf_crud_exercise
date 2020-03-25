
from rest_framework import viewsets

from recipapp.models import Recipe
from recipapp import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for all recipes endpoints"""

    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()

    def get_queryset(self):
        """Retrieve ingredients and populate into the queryset"""

        queryset = self.queryset
        filter_name = self.request.query_params.get('name', '')
        if filter_name:
            queryset = queryset.filter(name__startswith=filter_name)

        return queryset
