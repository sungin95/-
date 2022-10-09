from django.shortcuts import render, redirect
from .models import Input_food
from .forms import Input_food_model


def index(request):
    all_ = Input_food.objects.all()
    input_ = Input_food_model()
    content = {
        "food__list": all_,
        "food__list__forms": input_,
    }
    return render(request, "input/index.html", content)


def create(request):
    food_input = request.GET.get("food-input")
    food = food_input.split(",")
    for f in food:
        f = f.strip()
        print(f)
        Input_food.objects.create(
            name=f,
        )

    return redirect("input:index")


def delete(request, pk):
    delete_ingredient = Input_food.objects.get(pk=pk)
    delete_ingredient.delete()

    return redirect("input:index")
