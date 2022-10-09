from django.db import models


class Input_food(models.Model):
    name = models.CharField(max_length=30)
    amount = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField(null=True)
