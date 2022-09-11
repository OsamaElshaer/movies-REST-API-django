from datetime import time
from .models import *
from rest_framework import serializers


class AllMovies(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields =['id','title','gener','quality','category','contry','rate','time','year','Directors','Actors','overview','image','Iframemovie','slug']


class Featuredmovies(serializers.ModelSerializer):
    class Meta :
        model=Featured
        fields =['id','title','gener','quality','category','contry','rate','time','year','Directors','Actors','overview','image','Iframemovie','slug']