from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets, mixins

from recipapp.models import Recipe
from recipapp.serializers import RecipeSerializer


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

class RecipeViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin):
    """View for all recipes endpoints"""

    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
