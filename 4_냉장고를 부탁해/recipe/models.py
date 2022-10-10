from django.db import models


class Food_Ingredients(models.Model):
    name = models.CharField(max_length=30)
    amount = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField(null=True)


class Food_Recipe(models.Model):
    name = models.CharField(max_length=30)
    ingredients = models.TextField()
    picture = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
