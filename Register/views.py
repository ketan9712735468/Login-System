from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home_page(request):
    return render(request,'home.html',{})

def logoutuser(request):
    logout(request)
    return redirect('login')

def login_page(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username OR password is incorrect')

    return render(request,'login_page.html',{})


def register_page(request):
    form=RegisterForm()

    if request.method=="POST":
       form =RegisterForm(request.POST)
       if form.is_valid():
            form.save()
            user =form.cleaned_data.get('username')
            messages.success(request,'Account created for ' +user)
            return redirect(login_page)

    content={'form':form}
    return render(request,'register_page.html',content)