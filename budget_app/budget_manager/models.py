from django.db import models

# Create your models here.
class Transaction(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
