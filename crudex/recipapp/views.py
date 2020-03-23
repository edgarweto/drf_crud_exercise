from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets, mixins

from recipapp.models import Recipe
from recipapp import serializers


# @csrf_exempt
# @api_view(['GET', 'POST'])
# def recipe_list(request):
#     """
#     Experiment with function views before using DRF ViewSets
#     List all the recipes
#     """

#     if request.method == 'GET':
#         recipes = Recipe.objects.all()
#         serializer = RecipeSerializer(recipes, many=True)

#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         try:
#             print('\n >>> POST request')
#             # print(request.data)

#             print('\n >>> serialize')
#             print(request.data)
#             serializer = RecipeSerializer(data=request.data)

#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data, status=status.HTTP_200_OK)

#             print('\n >>> NOT VALID DATA!')
#             return JsonResponse(serializer.errors, status=status.HTTP_400_BAR_REQUEST)
#         except Exception as e:
#             print('\n >>> EXCEPTION')
#             print(str(e))
#             return JsonResponse(sys.exc_info()[0], status=status.HTTP_500_INTERNAL_ERROR)

class RecipeViewSet(viewsets.ModelViewSet):
    """View for all recipes endpoints"""

    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()

    def get_serializer_class(self):
        """Return appropiate serializer depending on the endpoint"""

        if self.action == 'retrieve':
            return serializers.RecipeDetailSerializer

        return self.serializer_class

    # def perform_create(self, serializer):
    #     """Support and specialize creating new recipes"""
    #     serializer.save()

    # def get_queryset(self):
    #     """Retrieve ingredients and populate into the queryset"""

    #     queryset = self.queryset

    #     return queryset