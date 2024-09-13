from django.db import models

# Create your models here.
class Transaction(models.Model):
    order = models.IntegerField()
    transaction_datetime = models.DateTimeField()
    comment = models.TextField()
    amount = models.BigIntegerField()
    offset_name = models.TextField(max_length=255)
