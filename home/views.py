from django.contrib.auth.models import User
from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login 

# Create your views here.
def index(request):
    return render(request,'index.html')

def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Login successfully")
        else:
            return redirect('signup')

    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('signup')

        # Create a new user
        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        messages.success(request, 'Account created successfully.')
        return redirect('login')
    return render(request,'register.html')