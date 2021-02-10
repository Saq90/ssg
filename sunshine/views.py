
from django.shortcuts import render,redirect
from .models import Contact

def home(request):
    return render(request,'home.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        message=request.POST.get('message', '')

        contact = Contact(name=name,email=email,message=message)
        contact.save()
        return redirect('/')
    return render(request,'contact.html')
