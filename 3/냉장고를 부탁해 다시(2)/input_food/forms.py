from django import forms
from .models import Input_food


class Input_food_model(forms.ModelForm):
    class Meta:
        model = Input_food
        fields = [
            "name",
        ]
