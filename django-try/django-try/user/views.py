
from pickletools import read_uint1
from cv2 import meanShift
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth import login ,authenticate,logout
from django.contrib import messages
from zmq import PLAIN_PASSWORD
# Create your views here.
app_name = 'user'
from .forms import LoginForm, RegisterForm
def register(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User()
            newUser.__setattr__("username",username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.success(request,message="register SUCCCEEES")
            return redirect('index')
        context = {
            'form': form
        }
        return render(request,"register.html",context)

    else:
        form  = RegisterForm()
        context = {
            'form': form
        }
    """form = RegisterForm
    context = {
        'form' : form
    }"""

    return render(request,"register.html",context)


def loginm(request):
    form = LoginForm(request.POST or None)
    context={
        'form' : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        userobject = authenticate(request,username=username,password=password)
        if (login is None ): 
            messages.info("daxil etdiyiniz melumatlar duzgun deyil")
            return render(request,'login.html')
        login(request,userobject)
        messages.success(request,message="Ugurla giris etdiniz")
        
        return  redirect('index')
       

    return render(request,"login.html",context)

def logOut(request):
    logout(request)
    messages.success(request,message='cixis elediniz')
    return redirect("index")
    