from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expenditure(models.Model):
    date=models.DateField(auto_now=False, auto_now_add=False)
    particular=models.CharField( max_length=50)
    amount=models.FloatField(max_length=100)
    mode_of_payment=models.CharField( max_length=50)
    User = models.ForeignKey(
        User, on_delete=models.CASCADE)