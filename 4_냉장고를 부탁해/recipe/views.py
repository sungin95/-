from audioop import reverse
from django.shortcuts import render, redirect
from .models import Food_Ingredients, Food_Recipe
from .forms import Food_Recipe_Form


def index(request):
    all_ = Food_Ingredients.objects.all()
    content = {
        "food__list": all_,
    }
    return render(request, "recipe/index.html", content)


# 작성자: 이성인
# 재료는 하나하나 기록이 되어 있지만, 레시피의 재료는 한곳에 모아져 있다.
# 그리고 레시피는 현재 있는 재료 중에서 부족한게 적은 순으로 보여주고 싶었다.
# 그걸 위해 재료와 레시피 재료를 세트에 담아서 교집합을 이용해 갯수를 구해 주었다.
# 작성일: 2022.10.10
def check(request):
    ingredients = Food_Ingredients.objects.all()
    recipes = Food_Recipe.objects.all()
    ingredients_list = set()  # 내가 등록한 재료 모음
    recipe_ingredients_list = set()  # 레시피 재료 모음
    Rearrangement = []  # 부족한 재료가 적을 수록 먼저 보이게
    for ingredient in ingredients:
        ingredients_list.add(ingredient.name)
    for recipe in recipes:
        recipe_a = recipe.ingredients.split(",")
        for a in recipe_a:
            recipe_ingredients_list.add(a.strip())

        Rearrangement.append(
            [
                len(recipe_ingredients_list)
                - len(ingredients_list & recipe_ingredients_list),
                recipe,
            ]
        )
        recipe_ingredients_list = set()  # 레시피 재료 리셋
    # 정렬 시킬 다음, 부족한 갯수 숫자가 있으면 출력이 안되므로 빼 주었다.
    Rearrangement.sort()
    recipes_output = []
    for out in Rearrangement:
        recipes_output.append(out[1])
    content = {
        "recipes": recipes_output,
    }
    return render(request, "recipe/check.html", content)


def create(request):
    food_input = request.POST.get("food-input")
    food = food_input.split(",")
    for f in food:
        f = f.strip()
        Food_Ingredients.objects.create(
            name=f,
        )
    return redirect("recipes:index")


def delete(request, pk):
    delete_ingredient = Food_Ingredients.objects.get(pk=pk)
    delete_ingredient.delete()
    return redirect("recipes:index")


def registration(request):
    if request.method == "POST":
        recipe_form = Food_Recipe_Form(request.POST)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect("recipes:recipe")
    else:
        recipe_form = Food_Recipe_Form()
    context = {
        "recipe_form": recipe_form,
    }
    return render(request, "recipe/registration.html", context)


def recipe(request):
    all_ = Food_Recipe.objects.all()
    content = {
        "recipe__list": all_,
    }
    return render(request, "recipe/recipe.html", content)


def detail(request, pk):
    select_recipe = Food_Recipe.objects.get(pk=pk)

    ingredients = Food_Ingredients.objects.all()

    ingredients_list = set()  # 내가 등록한 재료 모음
    recipe_ingredients_list = set()  # 레시피 재료 모음

    for ingredient in ingredients:
        ingredients_list.add(ingredient.name)

    recipe_a = select_recipe.ingredients.split(",")
    for a in recipe_a:
        recipe_ingredients_list.add(a.strip())
    o = ingredients_list & recipe_ingredients_list
    x = recipe_ingredients_list - o

    content = {
        "select_recipe": select_recipe,
        "O": o,
        "X": x,
    }

    return render(request, "recipe/detail.html", content)


def update(request, pk):
    recipe = Food_Recipe.objects.get(pk=pk)
    if request.method == "POST":
        recipe_form = Food_Recipe_Form(request.POST)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect("recipes:detail")
    else:
        recipe_form = Food_Recipe_Form(instance=recipe)
    context = {
        "recipe_form": recipe_form,
    }
    return render(request, "recipe/update.html", context)


def recipe_delete(request, pk):
    recipe = Food_Recipe.objects.get(pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect("recipes:recipe")

    return render(request, "recipe/update.html")
