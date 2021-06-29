
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Owe(models.Model):
    date=models.DateField(auto_now=False, auto_now_add=False)
    lender=models.ForeignKey(
        User, related_name='lender', on_delete=models.CASCADE)
    borrower=models.ForeignKey(
        User, related_name='borrower', on_delete=models.CASCADE)
    user_id=models.ForeignKey(
        User, related_name='user', on_delete=models.CASCADE)
    amount=models.FloatField(max_length=100)
    mode_of_payment=models.CharField( max_length=50)
   