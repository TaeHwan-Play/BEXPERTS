from django.db import models

# Create your models here.

class Image(models.Model):
  title = models.CharField(max_length=50)
  image = models.ImageField(upload_to="post/")
  isTrue = models.BooleanField()