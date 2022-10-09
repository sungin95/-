from urllib import request
from django.shortcuts import render
from input_food.models import Input_food


def index(request):
    all_ = Input_food.objects.all()
    ingredients = []
    for f in all_:
        ingredients.append(f.name)
    print(ingredients)
    return render(request, "output/index.html")


def registration(request):

    return render(request, "output/registration.html")
