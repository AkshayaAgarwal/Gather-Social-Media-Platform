from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
from django.db import IntegrityError
from Users.models import Myuser,Userinfo

def Users(request):
    if request.method== "POST" :
        try:
            if request.POST.get('password2')== request.POST.get('password'):
                auser = Myuser(username=request.POST.get('username'),email=request.POST.get('email'),password=request.POST.get('password'))
                auser.save();
                auser2 = Userinfo(email=request.POST.get('email'),college=request.POST.get('college'),course = request.POST.get('course'),date = request.POST.get('date'),gender= request.POST.get('gender'))
                auser2.save();
                return render(request,"register.html",{'info':'The user '+request.POST.get('username')+' has been registered successfully'})
            else:
                return render(request,"register.html",{'error':'Password Mismatch !'})
        except IntegrityError:
            return render(request,"register.html",{'error':'The user '+request.POST.get('username')+' exits !'})
    else:
        return render(request,"register.html")


# Create your views here.
