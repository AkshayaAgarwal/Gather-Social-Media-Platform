from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.template import loader
from django.db import IntegrityError
from Users.models import Users_table
from Users.models import Posts,Friends,Comments
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password  
import os
import datetime


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
    global user_email;
    global user_photo;
    global allposts2;
    global user_name;
    global allusers;
    global comments2;
    if request.method == 'POST':
        allposts = Posts.objects.all()
        friends = Friends.objects.all()
        friends2=[]
        for i in range(0,len(friends)):
            if friends[i].email1_id == request.POST.get('email'):
                friends2.append(friends[i].email2)
        
        comments2=Comments.objects.all()
        allposts2=[]
        
        for i in range(0,len(allposts)):
            
            if allposts[i].email.email in friends2:
                
                allposts2.append(allposts[i])
        
        allusers=Users_table.objects.all()
        flag=0
        for i in range(0,len(allusers)):
           
            if check_password(request.POST.get('password'),allusers[i].password) and allusers[i].username==request.POST.get('username') and allusers[i].email==request.POST.get('email'):
               flag=flag+1
               user_email = request.POST.get('email');
               user_photo = allusers[i].images;
               user_name=allusers[i].username;
               return render(request,"dashboard.html",{'comments':comments2,'allusers':allusers,'info2':request.POST.get('email'),'info':'User '+request.POST.get('username')+ ' logged in successfully !','img_obj':allusers[i].images,'allposts':allposts2})
        if flag==0:
            return render(request,"login.html",{'info':'Incorrect username or password !'})
    else:
        return render(request,"login.html")
    

def Add_post(request):
    if request.method == 'POST':
        mypost = request.FILES.get('mypost')
        mycap=''
        if len(request.POST.get('caption'))!= 0:
            mycap = request.POST.get('caption')
        date2 = datetime.datetime.now()
        allusers=Users_table.objects.all()
        comments2=Comments.objects.all()

        
        for i in range(0,len(allusers)):
            if allusers[i].email==user_email:
                apost=Posts(email=allusers[i],username = allusers[i].username,date=date2,posts=mypost,caption=mycap,total_likes =0)
                apost.save();
                return render(request,"makepost.html",{'comments':comments2,'allusers':allusers,'info':'User '+user_name+ ' logged in successfully !','allposts':allposts2,'img_obj':user_photo,'info2':'Post uploaded sucesssfully !','my_post':request.FILES.get('mypost')})
    else:
        allusers=Users_table.objects.all();
        comments2=Comments.objects.all();
        return render(request,"makepost.html",{'comments':comments2,'allusers':allusers,'info':'User '+user_name+ ' logged in successfully !','img_obj':user_photo,'allposts':allposts2})
    
def Search_friend(request):
    global allusers2;
    comments2=Comments.objects.all()
    allusers=Users_table.objects.all()
    if request.method == 'POST':
        college2=request.POST.get('college')
        course2 = request.POST.get('course')
        allusers = Users_table.objects.all()
        allusers2=[]
        friend_list=Friends.objects.all()
        friend_list2=[]
        for i in range(0,len(friend_list)):
            if friend_list[i].email1_id == user_email:
                friend_list2.append(friend_list[i].email2)
        
        for i in range(0,len(allusers)):
            if allusers[i].college == college2 and allusers[i].course == course2 and allusers[i].email != user_email:
                if allusers[i].email not in friend_list2:
                    allusers2.append(allusers[i])
        return render(request,'search_friends.html',{'comments':comments2,'allusers':allusers,'info':'User '+user_name+ ' logged in successfully !','allusers2':allusers2,'img_obj':user_photo,'allposts':allposts2})
    else:
        return render(request,'search_friends.html',{'comments':comments2,'allusers':allusers,'info':'User '+user_name+ ' logged in successfully !','img_obj':user_photo,'allposts':allposts2})
    
    
def Add_friend(request):
    
    if request.method=='POST':
        allusers=Users_table.objects.all() 
        for i in range(0,len(allusers)):
            if allusers[i].email==user_email:
                x=Friends(email1=allusers[i],email2=request.POST.get('friend'))
                x.save()
                
                for j in range(0,len(allusers2)):
                    if allusers2[j].email == request.POST.get('friend'):
                        allusers2.remove(allusers2[j])
                        break
                
                friends = Friends.objects.all()
                friends2=[]
                for i in range(0,len(friends)):
                    if friends[i].email1_id == user_email:
                         friends2.append(friends[i].email2)
                
                
                allposts = Posts.objects.all()
                allposts2=[]
        
                for i in range(0,len(allposts)):
                    if allposts[i].email.email in friends2:
                         allposts2.append(allposts[i])
                return render(request,'search_friends.html',{'comments':comments2,'allusers':allusers,'info':'User '+user_name+ ' logged in successfully !','allusers2':allusers2,'img_obj':user_photo,'allposts':allposts2})
    else:
        return render(request,'search_friends.html',{'comments':comments2,'allusers':allusers,'info':'User '+user_name+ ' logged in successfully !','allusers2':allusers2,'img_obj':user_photo,'allposts':allposts2})
                
def Add_comment(request):
    if request.method=='POST':
        val = request.POST.get('comment')
        postid=Posts.objects.all()
        for i in range(0,len(postid)):
            if str(postid[i].post_id)==request.POST.get('pid'):
                postid=postid[i]
                break
        
        for i in range(0,len(allusers)):
            if allusers[i].email==user_email:
                user_email2=allusers[i];
        date2=datetime.datetime.now()
        c=Comments(category='comment',comment=val,post_id=postid,email=user_email2,date=date2)
        c.save();
        comments2=Comments.objects.all();
        
        return render(request,'dashboard.html',{'comments':comments2,'allusers':allusers,'info2':user_email,'info':'User '+user_name+ ' logged in successfully !','img_obj':user_photo,'allposts':allposts2})
    else:
        return render(request,'dashboard.html',{'comments':comments2,'allusers':allusers,'info2':user_email,'info':'User '+user_name+ ' logged in successfully !','img_obj':user_photo,'allposts':allposts2})

def Add_like(request):
    if request.method=='POST':
        flag=0
        comments2=Comments.objects.all()
        for i in range(0,len(comments2)):
            if comments2[i].email.email == user_email and comments2[i].category=='like':
                flag=1
                break
        if flag==0:
            postid=Posts.objects.all()
            for i in range(0,len(postid)):
                if str(postid[i].post_id)==request.POST.get('pid'):
                    postid[i].total_likes = postid[i].total_likes+1
                    postid=postid[i]
                    break
            for i in range(0,len(allusers)):
                if allusers[i].email==user_email:
                    user_email2=allusers[i]; 
            c=Comments(category='like',comment='This post was liked',post_id=postid,email=user_email2)
            c.save()
            comments2=Comments.objects.all()
        return render(request,'dashboard.html',{'comments':comments2,'allusers':allusers,'info2':user_email,'info':'User '+user_name+ ' logged in successfully !','img_obj':user_photo,'allposts':allposts2})
    else:
        return render(request,'dashboard.html',{'comments':comments2,'allusers':allusers,'info2':user_email,'info':'User '+user_name+ ' logged in successfully !','img_obj':user_photo,'allposts':allposts2})