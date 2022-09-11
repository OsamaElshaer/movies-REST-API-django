from django.contrib.auth import authenticate, login
from django.urls.base import reverse
from Accounts.forms import SignupForm
from django.db.models.fields import related
from django.shortcuts import redirect, render
from .models import *
from .forms import FeaturedFilter, MovieFilter
from django.core.paginator import Paginator
# Create your views here.



def Movies(request):
    
    

    Movies=Movie.objects.all()
    myfilter=MovieFilter(request.GET , queryset=Movies)
    Movies=myfilter.qs

    paginator = Paginator(Movies, 18) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={
        'myfilter':myfilter,
        'page_obj': page_obj,
    }
    return render (request ,'moviegridfull.html' , context )


def singlemovie(request , slug):

    movie=Movie.objects.get(slug = slug)
    related=Movie.objects.filter(category=movie.category).filter(year=movie.year).filter(rate=movie.rate).exclude(slug=slug)[:10]
    context={
       
        'movies':movie,
        'cate':related,
    }
    return render(request ,'singlemovie.html',context)


def FurMovie(request): 

    furmovie=Featured.objects.all()

    myfilter=FeaturedFilter(request.GET , queryset=furmovie)
    moviel_list=myfilter.qs

    paginator=Paginator(moviel_list , 18)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
        'myfilter':myfilter,
        'page_obj':page_obj,

    }
    return render(request , 'furmovie.html' ,context)


def fursingle(request ,slug):



    furmovie=Featured.objects.get(slug=slug)
    related=Featured.objects.filter(category=furmovie.category).exclude(slug=slug)[:10]
    context={
        'movies':furmovie,
        'cate':related


    }
    return render (request , 'fursingle.html',context)