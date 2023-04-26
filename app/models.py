from django.db import models
from django.core import validators
# Create your models here.
class Topic(models.Model):
    name=models.CharField(max_length=20,validators=[validators.MinLengthValidator(5)])
    age=models.IntegerField(validators=[validators.MinValueValidator(18)])
    mobileno=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
