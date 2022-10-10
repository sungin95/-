from django.urls import path
from . import views

app_name = "recipes"


urlpatterns = [
    path("", views.index, name="index"),
    path("check/", views.check, name="check"),
    path("create/", views.create, name="create"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("recipe/", views.recipe, name="recipe"),
    path("recipe/registration/", views.registration, name="registration"),
    path("recipe/detail/<int:pk>/", views.detail, name="detail"),
    path("recipe/detail/<int:pk>/update/", views.update, name="update"),
    path("recipe/detail/<int:pk>/delete/", views.recipe_delete, name="recipe-delete"),
]
