from django.db import models
from django.contrib.auth.models import AbstractUser

class StripDetails(models.Model):
    customer_id = models.CharField(max_length = 100)
    name = models.CharField(max_length=100, blank=True)


class TestModel(models.Model):
    image = models.FileField(upload_to="images")    
    image_m = models.ImageField(upload_to="images", blank=True, null=True)

# class User(AbstractUser):


from django.contrib.postgres.fields import ArrayField

class AbilityModel(models.Model):
    question = models.CharField(max_length=255, default="")
    answer_option=ArrayField(models.CharField(max_length=255,default=""), blank=True, null=True)
    corect_answer = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_mcq = models.BooleanField(default=False)
    is_arabic = models.BooleanField(default=False)

    class Meta:
        db_table = "Ability"
