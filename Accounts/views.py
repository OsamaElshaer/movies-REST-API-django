from typing import Reversible
from django.contrib.auth import authenticate , login
from django.forms.forms import Form
from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.urls import reverse

# Create your views here.
def signup(request):

    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request, user)
            return redirect(reverse('profile'))
            
    else:
        form=SignupForm()


    context={
        'form':form
    }
    return render (request,'registration/signup.html',context)


def Profile(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']  
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse( 'accounts:profile'))

    else:
        form=SignupForm()


    context ={
        'form':form,
        'profile':profile.objects.get(user=request.user)
    }
    return render (request ,'profile/userprofile.html',context )


def profile_edit(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']  
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse( '/profile'))

    else:
        form=SignupForm()


    Profile=profile.objects.get(user=request.user)

    if request.method=='POST':
        userform=UserForm(request.POST,instance=request.user)
        profileform=ProfileForm(request.POST,request.FILES,instance=Profile)

        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile=profileform.save(commit=False)
            myprofile.user=request.user
            myprofile.save()

            return redirect('/profile')

    else:
        userform=UserForm(instance=request.user)
        profileform=ProfileForm(instance=Profile)

    context={
        'profile':profile.objects.get(user=request.user),
        'userform':userform,
        'profileform': profileform,
        'form':form,
    }
    return render (request ,'profile/userprofileedit.html', context)