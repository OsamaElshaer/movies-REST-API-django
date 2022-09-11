from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.urls.base import reverse
from Accounts.forms import SignupForm



def authuser(request):
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
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')      
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user,backend=None)
            return redirect(reverse( 'accounts:profile'))
        else :
            pass

    return {"form":form}