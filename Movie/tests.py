from django.http import response
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse
from django.utils.text import slugify
from Movie.forms import MovieFilter, MovieForm
from Movie.models import Movie, Quality
from Movie.views import Movies

# Create your tests here.

