from typing import ChainMap, Reversible
from django.db import models
from django.db.models.deletion import PROTECT, RESTRICT
from django.db.models.fields import CharField, DecimalField, IntegerField, TimeField, URLField
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
def images_movie(instance , filename):
    imagename , extension = filename.split(".")
    return "Movieimages/%s.%s"%(instance.id,extension)

class Featured(models.Model):
    
    title=models.CharField(max_length=200)
    gener=models.CharField(max_length=100,null=True , blank=True)
    quality=models.ForeignKey('Quality',on_delete=models.PROTECT,null=True , blank=True)
    category=models.ForeignKey('Category',on_delete=models.PROTECT,null=True , blank=True)
    contry=models.ForeignKey('Contry',on_delete=PROTECT,null=True , blank=True)
    rate=models.CharField(max_length=5, null=True , blank=True)
    time=models.CharField(max_length=10 , null=True , blank=True)   
    year=models.ForeignKey( 'Year',on_delete=PROTECT,null=True , blank=True)
    Directors=models.CharField(max_length=200 , null=True , blank=True)
    Actors=models.CharField(max_length=300 , null=True , blank=True)
    overview=models.TextField(max_length=1000 , null=True , blank=True)
    image=models.URLField(null=True , blank=True)
    Iframemovie=URLField(max_length=500, null=True , blank=True)
    slug=models.SlugField(null=True , blank=True)

    def __str__ (self):
        return self.title
    def save (self , *args, **kwargs):       
        self.slug =slugify(self.title) 
        super(Featured,self).save(*args,**kwargs)
class Movie(models.Model):
    
    title=models.CharField(max_length=300)
    gener=models.CharField(max_length=100,null=True , blank=True)
    quality=models.ForeignKey('Quality',on_delete=models.PROTECT,null=True , blank=True)
    category=models.ForeignKey('Category',on_delete=models.PROTECT,null=True , blank=True)
    contry=models.ForeignKey('Contry',on_delete=PROTECT,null=True , blank=True)
    rate=models.CharField(max_length=5, null=True , blank=True)
    time=models.CharField(max_length=10 , null=True , blank=True)   
    year=models.ForeignKey( 'Year',on_delete=PROTECT,null=True , blank=True)
    Directors=models.CharField(max_length=200 , null=True , blank=True)
    Actors=models.CharField(max_length=300 , null=True , blank=True)
    overview=models.TextField(max_length=1000 , null=True , blank=True)
    image=models.URLField(null=True , blank=True)
    Iframemovie=URLField( null=True , blank=True)
    slug=models.SlugField(max_length=5, null=True , blank=True)
    

    def __str__(self):
        return str(self.title)

    def save (self , *args, **kwargs):       
        self.slug =slugify(self.title) 
        super().save(*args,**kwargs)

    class Meta:
        ordering=('id',)
    
    def get_absolute_url(self):
        return reverse('Movie:movie',kwargs={'slug':self.slug})
        

class Category(models.Model):
    name=models.CharField(max_length=20,null=True , blank=True)
    def __str__(self):
        return str(self.name)

class Quality(models.Model):
    name=models.CharField(max_length=20,null=True , blank=True)
    def __str__(self):
        return str(self.name)

class Contry(models.Model):
    num=models.CharField(max_length=50)
    def __str__(self):
        return str(self.num)

class Year(models.Model):
    num=models.CharField(max_length=5)
    def __str__(self):
        return str(self.num)
