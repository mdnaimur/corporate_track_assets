from django.shortcuts import render, redirect
from django.http.response import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import MyUserFrom
# Create your views here.


# ? Home page
def home(request):

    return render(request, 'base/home.html')


# User Registration function

def registerUser(request):
    form = MyUserFrom()
    if request.method == 'POST':
        form = MyUserFrom(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registraion')
    context = {'form': form}
    return render(request, 'base/register.html', context)


# ? Login user function code

def loginUser(request):

    # after registration user can directly login
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        # getting user information from user
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        # mathing database if user exist or not
        try:
            user = user.object.get(email=email)
        except:
            messages.error(request, 'User does not exist.')

        # user email and password match from database
        user = authenticate(request, email=email, password=password)
        # user validation check
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exits')
    return render(request, 'base/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
