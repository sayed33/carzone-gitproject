from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    designation = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%M/%D/')
    facebook = models.URLField(max_length=255)
    linkedin = models.URLField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
