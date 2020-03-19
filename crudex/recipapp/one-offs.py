# """
# As we are not implementing CRUD for ingredients, we need a way to
# populate our DB. This file implements that set up
# """

# from recipapp.models import Ingredient
# from recipapp.serializers import IngredientSerializer


# # Create some ingredients
# # ingredient = Ingredient(name='Salt')
# # ingredient.save()
# basicIngredients = ['sugar', 'olive oil', 'vinegar', 'bread', 'flour']

# for ingrName in basicIngredients:
#     ingredient = Ingredient(name=ingrName)
#     ingredient.save()

# allIngredients = Ingredient.objects.all()
# serializer = IngredientSerializer(allIngredients, many=True)

# print('\n\n >>> GENERATED INGREDIENTS')
# print(serializer.data)