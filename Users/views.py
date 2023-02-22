from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.template import loader
from django.db import IntegrityError
from Users.models import Users_table
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password  
import os



def Users(request):
    if request.method== "POST" :
        try:
            if request.POST.get('password2')== request.POST.get('password'):
                allusers=Users_table.objects.all()
                flag=0
                for i in range(0,len(allusers)):
                    if allusers[i].email == request.POST.get('email'):
                        flag=1
                        break
                if flag==1:
                    return render(request,"register.html",{'error':'This email id is already registered !'})
                else:
                    auser = Users_table(username=request.POST.get('username'),email=request.POST.get('email'),password=make_password(request.POST.get('password')),college=request.POST.get('college'),course=request.POST.get('course'),date=request.POST.get('date'),gender=request.POST.get('gender'),images=request.FILES.get('image'),phone=request.POST.get('number'))
                    auser.save();
                    return render(request,"register.html",{'info':'The user '+request.POST.get('username')+' has been registered successfully'})
            else:
                return render(request,"register.html",{'error':'Password Mismatch !'})
        except IntegrityError:
            return render(request,"register.html",{'error':'The user '+request.POST.get('username')+' exits !'})
    else:
        return render(request,"register.html")


# Create your views here.
def Login(request):
    if request.method == 'POST':
        allusers=Users_table.objects.all()
        flag=0
        for i in range(0,len(allusers)):
           
            if check_password(request.POST.get('password'),allusers[i].password) and allusers[i].username==request.POST.get('username') and allusers[i].email==request.POST.get('email'):
               flag=flag+1
               return render(request,"dashboard.html",{'info':'User logged in successfully !','img_obj':allusers[i].images})
        if flag==0:
            return render(request,"login.html",{'info':'Incorrect username or password !'})
    else:
        return render(request,"login.html")


