from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.forms import fields, widgets
from .models import *

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'type':"text",
            'name':"username",
            'id':"username" ,
            'placeholder':'username',
            'style':"border-radius: 10px;",
        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'type':"text",
            'name':"email",
            'id':"email-2" ,
            'placeholder':'Email',
            'style':"border-radius: 10px;",

        })        
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'type':"text",
            'name':"password",
            'id':"password-2" ,
            'placeholder':'Password',
            'style':"border-radius: 10px;",

        })
        self.fields["password2"].widget.attrs.update({
            'required':'',
            'type':"text",
            'name':"password",
            'id':"repassword-2" ,
            'placeholder':'Re-password',
            'style':"border-radius: 10px;",

        })
    class Meta:
        model=User
        fields=['username','email', 'password1','password2']




class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']




class ProfileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields='__all__'  
    