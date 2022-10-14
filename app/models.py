from email.mime import image
from re import T
from turtle import title
from django.db import models

# Create your models here.

class Home (models.Model):
    image=models.ImageField(upload_to='media/%d/%m/%y')
    title=models.CharField(max_length=15,null=True)

    def __str__(self):
        return str(self.image)


class Contact (models.Model):
    phone= models.IntegerField()
    adress = models.CharField(max_length=100,null=True)
    open_time = models.TimeField(blank=True,null=True)
    emaill = models.EmailField(null=True)

    def __str__(self):
        return str(self.phone) 

          