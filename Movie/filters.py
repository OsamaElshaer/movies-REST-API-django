import django_filters
from .models import Movie

class MovieFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Movie
        fields =['title','Category','rate','quality','year']
        #exclude=[['invalid name']]