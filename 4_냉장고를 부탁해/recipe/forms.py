from .models import Food_Recipe
from django import forms


class Food_Recipe_Form(forms.ModelForm):
    class Meta:
        model = Food_Recipe
        fields = [
            "name",
            "picture",
            "ingredients",
        ]
