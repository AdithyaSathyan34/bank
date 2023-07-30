from django.contrib import messages, auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from bankingapp.models import bank_detail


# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid data")
            return redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if(password==cpassword):
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return  redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save();
                return redirect('new')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def form(request):
        if request.method == 'POST':

            name = request.POST.get('name')
            phone = request.POST.get('phone')
            dob = request.POST.get('dob')
            mail = request.POST.get('mail')
            address = request.POST.get('address')
            gender = request.POST.get('gender')
            district = request.POST.get('district')
            branch = request.POST.get('branch')
            accountype = request.POST.get('accounttype')
            material = request.POST.get('material')

            bank= bank_detail.objects.create(name=name, phone=phone, dob=dob, mail=mail,address=address, gender=gender,district=district,
                                                      branch=branch, accounttype=accountype, material=material)

            return redirect('order')
        else:
            return render(request, 'form.html')

        return render(request, 'form.html')


def new(request):
    return render(request,'new.html')
def order(request):
    return render(request,'order.html')

def logout1(request):
    logout(request)
    return render(request,'login.html')