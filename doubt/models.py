from django.db import models

# Create your models here.
class question(models.Model):
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='img', blank=True)
