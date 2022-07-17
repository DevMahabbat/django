from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
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
    form = Articleform(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla oluşturuldu")
        return redirect("index")
    return render(request,"addarticle.html",{"form":form})