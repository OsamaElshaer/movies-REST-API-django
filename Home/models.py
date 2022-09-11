from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import DecimalField, TimeField, URLField
from django.utils.text import slugify
from Movie.models import Movie
# Create your models here.
def images_movie(instance , filename):
    imagename , extension = filename.split(".")
    return "Movieimages/%s.%s"%(instance.id,extension)

def images_slider(instance , filename):
    imagename , extension = filename.split(".")
    return "sliderimages/%s.%s"%(instance.id,extension)

def images_trailer(instance , filename):
    imagename , extension = filename.split(".")
    return "terialimages/%s.%s"%(instance.id,extension)




class Slider(models.Model):



    quality_choices=[
        ('HD','HD'),
        ('HDRip','HDRip'),
        ('SD','SD'),
        ('TS','TS'),
        ('CAM','CAM'),
    ]
    
    quntry=[
        ('Europ','Europ'),
        ('International','International'),
        ('United State','United State'),
    ]
    type_choices=[
        ('Movie','Movie'),
        ('TV-Series','TV-Series'),
    ]
    status_choices=[
        ('Watch Now','Watch Now'),
        ('Coming Soon','Coming Soon'),
    ]
    title=models.CharField(max_length=200)
    rate=models.DecimalField(max_digits=10, decimal_places=1 , null=True , blank=True)
    quality=models.CharField(max_length=10 ,choices= quality_choices, null=True , blank=True)
    image_url=models.URLField(max_length=300, null=True , blank=True)
    image=models.ImageField(upload_to=images_slider, null=True , blank=True)
    imageposter=models.URLField(max_length=300, null=True , blank=True)
    time=models.CharField(max_length=10,null=True , blank=True)
    category=models.ForeignKey('Category' , on_delete=models.PROTECT , null=True , blank=True)
    desc=models.TextField(max_length=500 , null=True , blank=True)
    gener=models.CharField(max_length=200, null=True , blank=True)
    directors=models.CharField(max_length=200, null=True , blank=True)
    actors=models.CharField(max_length=300, null=True , blank=True)
    quntry=models.CharField(max_length=15 , choices=quntry , null=True , blank=True)
    status=models.CharField(max_length=15 , choices=status_choices , null=True , blank=True)
    year=models.IntegerField( null=True , blank=True)
    type=models.CharField(max_length=15 , choices=type_choices , null=True , blank=True)
    iframeurl=models.URLField(max_length=500 , null=True , blank=True)
    slug=models.SlugField(null=True , blank=True)
    def __str__(self):
        return str(self.title)

    def save (self , *args, **kwargs):       
        self.slug =slugify(self.title) 
        super(Slider,self).save(*args,**kwargs)


class Category(models.Model):
    name=models.CharField(max_length=20,null=True , blank=True)
    def __str__(self):
        return str(self.name)

class trailer(models.Model):
    title=models.CharField(max_length=200)
    image_url=models.URLField(max_length=300,null=True , blank=True )
    image=models.ImageField(upload_to=images_trailer , null=True , blank=True)
    time=models.CharField(max_length=10, null=True , blank=True)
    iframe=URLField(max_length=500)

    def __str__(self):
        return str(self.title)
