from django.db import models
 
# Create your models here.
class Students(models.Model):
    name=models.TextField()
    email=models.EmailField()
    age=models.IntegerField()
    phone=models.IntegerField()

