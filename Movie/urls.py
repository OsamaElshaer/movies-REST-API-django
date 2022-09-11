from django.urls import path

from . import views
from . import api

app_name='Movie'

urlpatterns = [

    
    path('', views.Movies, name='movie'),
    path('featured',views.FurMovie,name='featured' ),
    path('ML<str:slug>', views.singlemovie, name='singlemovie'), 
    path('Fu<str:slug>',views.fursingle,name='fursingle'),   


    path('api/movies' ,api.all_movies , name='allmovies'),
    path('api/movies/<int:id>' ,api.movie_detail , name='movie_detail'),

    path('api/featured' ,api.featured_movies , name='featured'),
  

]