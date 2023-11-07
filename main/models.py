from django.db import models

# Create your models here.
class member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=255)


class news(models.Model):
    catagory = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    language_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    content = models.TextField()

    