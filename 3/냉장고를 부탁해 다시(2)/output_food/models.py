from django.db import models


class Output_food(models.Model):
    name = models.CharField(max_length=30)
    ingredients = models.CharField(max_length=30)
    picture = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
