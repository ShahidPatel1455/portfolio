from django.shortcuts import render,redirect,HttpResponse
from app01.models import Contactwala

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def resume(request):
    return render(request,'resume.html')

def services(request):
    return render(request,'services.html')

def contact(request):

    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fsubject=request.POST.get('subject')
        fmessage=request.POST.get('message')
        
        query=Contactwala(name=fname,email=femail,subject=fsubject,message=fmessage)
        query.save()

        return render(request,'contactsave.html')

 
    return render(request,'contact.html')