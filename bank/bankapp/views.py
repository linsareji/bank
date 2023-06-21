import json
# from tkinter import messagebox

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import PersonCreationForm
from .models import *


# Create your views here.

# def index(request):
#     return render(request,'index.html')
# def index(request):
#     countries = Country.objects.values('id','name')
#     return render(request,"kyc.html",{'countries':countries})
def home(request):
    return render(request,'index.html')
def fetch_state(request):
    country_id = request.POST.get('country_id')
    states = list(State.objects.filter(country_id=country_id).values('name','id'))
    return JsonResponse({'states':states},safe=False)

def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('kyc')
        else:
            messages.info(request,'invaid credentials')
            return redirect('login')

    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=name).exists():
                messages.info(request,'user already exist')
                return  redirect('register')
            else:
                user=User.objects.create_user(username=name,password=password)
                user.save()
                print("user created")
                return redirect('login')
        else:
            print('Password mismatch')
            messages.info(request, 'Password mismatch')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def kyc(request):

    if request.method == 'POST':
        fname = request.POST['username']
        dob = request.POST['dob']
        mobileno = request.POST['mobileno']
        email = request.POST['email']
        address = request.POST['address']
        kyc = Kyc(fname=fname, dob=dob,mobile=mobileno,mailid=email,address=address)
        kyc.save()
        print("user saved")
        messages.info(request, 'Application Accepted')
        return redirect('home')
    countries = Country.objects.values('id', 'name')
    return render(request, "kyc.html", {'countries': countries})

    return render(request,'kyc.html')

def logout(request):
    return render(request,'index.html')
