from django.urls import path
from . import views
app_name='Home'

urlpatterns = [

    
    path('', views.landing, name='landing'),
    path('Index', views.Index, name='index'),
    path('404', views.P404, name='404'),
    path('SL<str:slug>', views.singleslider, name='singleslider'),  

]