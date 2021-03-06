from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from .models import Article,Author,Category
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    articles=Article.objects.all()
    return render(request, 'index.html' ,{'articles':articles})
def single(request,id):
    if request.user.is_anonymous:
        return redirect("/login")
    single=Article.objects.get(id=id)
    return render(request, 'single.html' ,{'single':single})
def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(password)
        print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
            #print(100)
            login(request,user)
        return redirect("/")
        else:
            #print("rahul")
            return render(request,'login.html')
    return render(request, 'login.html')
def signupuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        #print(password)
        #print(username,password)
        user = Author(username=username, password=password)
        author = User(username=username, email=email)
        user.save()
        author.save()
    return render(request, 'login.html')
def addarticlenew(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method=="POST":
        title=request.POST.get('username')
        img=request.POST.get('password')
        content=request.POST.get('username')
        user=request.POST.get('password')
        #print(password)
        #print(username,password)
        user = Article(title=title, image=img, content=content, author=user)
        Article.save()
    return render(request, 'index.html')
def logoutuser(request):
    logout(request)
    return redirect("/login")
