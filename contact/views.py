from django.shortcuts import render
from django.core.mail import send_mail
from Blockter import settings
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def contact(request):

    if request.method=='POST':
        subject=request.POST['Subject']
        email=request.POST['Email']
        message=request.POST['Message']

        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
    )
    return render (request , 'contact.html')