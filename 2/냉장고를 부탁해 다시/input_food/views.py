from django.shortcuts import render, redirect
from .models import Input_food

# Create your views here.
def index(request):

    return render(request, "input/index.html")


def create(request):
    food_input = request.GET.get("food-input")
    food = food_input.split(",")
    a = Input_food.objects.all()
    print(a)
    for f in food:
        print(type(f))
        # Input_food.objects.create(
        #     name=f,
        #     amount=f,
        #     expiration_date="2022-02-02",
        # )

    return redirect("input:index")
