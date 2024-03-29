from django.db import models

# Create your models here.

class StripDetails(models.Model):
    customer_id = models.CharField(max_length = 100)