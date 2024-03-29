from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages

# Create your views here.
def home(request):
    count = User.objects.count()
    return render(request, "home.html", {'count':count})


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form':form})


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in")
            return redirect('login')
     
    else:
        return render(request, 'login.html', {})
    

def user_logout(request):
     logout(request)
     messages.success(request, ("You have successfully logged out"))
     return redirect('home')