from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def register(request):
    if request.user.is_authenticated == True:
        return redirect("dashboard")
    if request.method=="POST":
        username =request.POST.get('username')
        email =request.POST.get('email')
        pass1  =request.POST.get('pass1')
        pass2  =request.POST.get('pass2')

        # if pass word do not match
        if pass1 != pass2:
            messages.warning(request, "Password do not match")
            return redirect('signup')

        # if the username is already taken
        if User.objects.filter(username = username).exists():
            messages.warning(request, "Username already exist")
            return redirect('signup')

        # if new user is registering 
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()

        messages.success(request, "Your account has been created successfully, Thanks for registring on MeetMaaya")
        # redirect user to login page after regiatred
        return redirect('signin')
    return render(request, "register.html")

@csrf_exempt
def signin(request):
    # sign in 
    if request.method=="POST":
        username =request.POST.get('uname')
        pass1  =request.POST.get('psw')

        user=authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid Credintials")
            return redirect('signin')

    return render(request, "signin.html")

def dashboard(request):

    if request.user.is_authenticated == False:
        return redirect("signin")
    
    return render(request, "dashboard.html")

def videocall(request):
    
    if request.user.is_authenticated == False:
        return redirect("signin")
    return render(request, "videocall.html", {'name':request.user.username})

def logout_user(request):
    logout(request)
    return redirect("signin")

def join_room(request):
    
    if request.user.is_authenticated == False:
        return redirect("signin")
    
    if request.method == 'POST':
        room_id =request.POST.get('room_id')
        return redirect("/meeting?roomID="+room_id)
        
    return render(request,"join_room.html",  {'name':request.user.username})

def avatar(request):
    
    if request.user.is_authenticated == False:
        return redirect("signin")
    
    return render(request, "avatar.html")