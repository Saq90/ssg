
from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages

def home(request):
    return render(request,'home.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        message=request.POST.get('message', '')
        if len(name)<3 or len(email)<3:
            messages.error(request, "Please fill the form correctly")
        else:
           contact = Contact(name=name,email=email,message=message)
           contact.save()
           messages.success(request, "Your message has been successfully sent")
           return redirect('/contact/')
    return render(request,'contact.html')
