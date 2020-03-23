from django.urls import path, include

from rest_framework.routers import DefaultRouter

from recipapp import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)

app_name = 'recipapp'
urlpatterns = [
    path('', include(router.urls))
]
