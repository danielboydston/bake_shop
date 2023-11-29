from django.db import models

# Create your models here.
class Config(models.Model):
  item = models.CharField(max_length=255)
  value = models.TextField()