
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth import login 
# Create your views here.
app_name = 'user'
from .forms import RegisterForm
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