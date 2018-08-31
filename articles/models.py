from django.db import models
from django.utils import timezone
# Create your models here.
class articles_News(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    detail= models.CharField(max_length=400)
    slug = models.SlugField()
    date= models.DateTimeField(default=timezone.now)
    picture = models.ImageField( default='default.png', blank=True)

    def __str__(self):
        return self.title



class articles_Analyse(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    detail= models.CharField(max_length=400)
    slug = models.SlugField()
    date= models.DateTimeField(default=timezone.now)
    picture = models.ImageField( default='default.png', blank=True)
    
    def __str__(self):
            return self.title




class articles_Tutorial(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    detail= models.CharField(max_length=400)
    slug = models.SlugField()
    date= models.DateTimeField(default=timezone.now)
    picture = models.ImageField( default='default.png', blank=True)

    def __str__(self):
            return self.title

