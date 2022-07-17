from django.shortcuts import render,HttpResponse

# Create your views here.
from .forms import  Articleform
def index(request):
    
    return  render(request,"index.html")
def about(request,id):
    context = {'id':id}
    return HttpResponse("about")
def dashboard(request):
    return render(request,"dashboard.html",)

def addArticle(request):
    form = Articleform
    context = {'form': form }
    return render(request,"addarticle.html",context)