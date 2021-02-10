from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')



from django.shortcuts import render,redirect
from .models import Contact
# Create your views here.

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        message=request.POST.get('message', '')

        contact = Contact(name=name,email=email,message=message)
        contact.save()
        return redirect('/')
    return render(request,'contact.html')
