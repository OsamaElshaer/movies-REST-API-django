from datetime import date
from  .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def all_movies(request):
    allmovie=Movie.objects.all()
    serapi=AllMovies(allmovie , many=True).data
    return Response({'AllMovies':serapi})

@api_view(['GET'])
def movie_detail(request,id):
    movie=Movie.objects.get(id=id)
    movie_detail=AllMovies(movie).data
    return Response({'Movie Details':movie_detail})




@api_view(['GET'])
def featured_movies(request):
    featured=Featured.objects.all()
    serapi=Featuredmovies(featured , many=True).data
    return Response({'Featured Movies':serapi})

