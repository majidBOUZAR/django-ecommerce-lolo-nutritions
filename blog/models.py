from audioop import maxpp
from distutils.command import upload
from email.mime import image
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class  Category (models.Model):
  name = models.CharField(max_length=200,null=True,blank=True)

  def __str__(self):
        return self.name
    


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="app/images/")
    published = models.DateField(auto_created=True,auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories',null=True,blank=True)
    slug = models.SlugField(blank=True,null=True)
    def save(self ,*args ,**kwargs):
        self.slug = slugify(self.title)
        super(Blog,self).save(*args,**kwargs)  
    def __str__(self):
        return self.title



class Comment (models.Model):  
    X = [
     ('Live','Live'),
     ('Stop','Stop'),
      ]      
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments',null=True,blank=True)
    comment_name=models.CharField(max_length=30,null=True)
    comment_mail=models.CharField(max_length=30,null=True)
    comment_date = models.DateField(auto_created=True,auto_now=True)
    image=models.ImageField(upload_to="app/images/",null=True)
    comment = models.TextField(max_length=5000)
    status = models.CharField(max_length=50,choices=X,null=True,blank=True)
    
    def __str__(self):
       return self.comment_mail
