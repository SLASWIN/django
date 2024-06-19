from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate,login

# Create your views here.
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        usertype=request.POST['usertype']
        
        user=User.objects.create_user(first_name=name,email=email,username=username,password=password,usertype=usertype)
        user.save()
        # return HttpResponse('success')
        return HttpResponse("<script>window.alert('successfully register');window.location.href='/rg/lg'</script>")
    
    else:
        return render(request,'register.html')

def log(request):
    if request.POST:
        ur=request.POST["username"]
        password=request.POST['pass']
        print(ur,password)
        u=authenticate(request,password=password,username=ur)
        print(u)
        if u is not None:
            if u.is_superuser==1:
                request.session['sid']=u.id
                print(request.session['sid'])
                login(request,u)
                return HttpResponse('LOGIN SUCCESSFULLY ADMIN')
            elif u.is_superuser==0 and u.usertype=="Jobseeker":
                request.session['sid']=u.id
                o=request.session['sid']
                print(o)
                login(request,u)
                return HttpResponse('login succesfully jobseeker')
            elif u.is_superuser==0 and u.usertype=="recruiter":
                request.session['sid']=u.id
                o=request.session['sid']
                print(o)
                login(request,u)
                return HttpResponse('login succesful recruiter')
        return HttpResponse('log in failed')
    else:
        return render(request,'login.html')

