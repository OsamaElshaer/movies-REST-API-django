from django.urls import path
from . import views
app_name='Accounts'

urlpatterns = [

    
    path('Signup', views.signup, name='signup'),
    path('profile', views.Profile, name='profile'),    
    path('profileEdit', views.profile_edit, name='edit'),
]