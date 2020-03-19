from django.urls import path
from recipapp import views

urlpatterns = [
    path('recipes/', views.recipe_list)
]