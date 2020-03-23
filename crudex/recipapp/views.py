from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets, mixins

from recipapp.models import Recipe
from recipapp import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for all recipes endpoints"""

    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()

    def get_serializer_class(self):
        """Return appropiate serializer depending on the endpoint"""

        if self.action == 'retrieve':
            return serializers.RecipeDetailSerializer

        return self.serializer_class

    def get_queryset(self):
        """Retrieve ingredients and populate into the queryset"""

        queryset = self.queryset
        filter_name = self.request.query_params.get('name', '')
        if filter_name:
            queryset = queryset.filter(name__startswith=filter_name)

        return queryset
