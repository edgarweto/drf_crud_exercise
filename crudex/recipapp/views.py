from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer

from recipapp.models import Recipe
from recipapp.serializers import RecipeSerializer

def recipe_list(request):
    """
    List all the recipes
    """

    if request.method == 'GET':

        # # Add just one:
        # # Recipe.objects.create(name='RecetaX', description='bla bla bla')
        # recipe1 = Recipe(name='RecetaX', description='bla bla bla')
        # recipe1.save()
        # recipeSerializer = RecipeSerializer(recipe1)
        # print('\n>>>>>>> recipe:')
        # print(recipeSerializer.data)

        # content = JSONRenderer().render(recipeSerializer.data)
        # print('\n>>>>>>> recipe content:')
        # print(content)

        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)

        return JsonResponse(serializer.data, safe=False)
