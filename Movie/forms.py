from django import forms
import django_filters
from .models import *

class MovieFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Movie
        fields =['title','category','quality','contry','year']
        #exclude=[['invali==d name']

class FeaturedFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Featured
        fields =['title','category','quality','contry','year']
        #exclude=[['invali==d name']
        

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['title','category','quality','contry','year']
