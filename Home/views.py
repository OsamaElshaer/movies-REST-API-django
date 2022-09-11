from django.contrib.auth import authenticate, login
from django.http import request
from django.http.response import HttpResponse
from django.urls import reverse
from Accounts.forms import SignupForm
from django.db.models.fields import related
from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator,PageNotAnInteger , EmptyPage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from Movie.models import * 
# Create your views here.

    
def Index(request):        

    featured=Featured.objects.all()
    featured=featured[:15]

    allmovie=Movie.objects.all()
    allmovie=allmovie[:15]


    context={
        'allmovies':allmovie,
        'featureds':featured,
        'sliders' :Slider.objects.all(),
        'trailers':trailer.objects.all(),
    }
    return render(request ,'Index.html' , context)

def landing(request):

        
    context={
    }   

    return render(request ,'landing.html',context)

def P404(request):
    
        
    return render(request ,'404.html')

def singleslider(request , slug):
    
    slider=Slider.objects.get(slug = slug)
    related11=Movie.objects.filter(rate=slider.rate).exclude(slug=slug)[:10]
    context={
       
        'slider':slider,
        'cate1':related11
        
    }
    return render(request ,'singleslider.html',context)



