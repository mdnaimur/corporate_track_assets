from django.shortcuts import render, redirect
from django.http.response import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import MyUserFrom, Poducts_Form, Employee_Form
from .models import User, Product_Assets, Employee
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


#! logout user

def logoutUser(request):
    logout(request)
    return redirect('login')


# def emoplyee_add
@login_required(login_url='/login')
def employee_add(request):
    form = Employee_Form()
    user = User.objects.all()

    if request.method == 'POST':
        form = Employee_Form(request.POST)
        messages.error(request, form.errors)
        if form.is_valid():
            employee = Employee.objects.create(
                host=request.user,
                name=request.POST.get('name'),
                designation=request.POST.get('designation'),
                department=request.POST.get('department'),
                phone_number=request.POST.get('phone_number')
            )
            return redirect('employee/employee_details')
        else:
            messages.error(
                request, 'An error occured during employee registration"')

    context = {"form": form}
    return render(request, 'employee/employee_add.html', context)


def employee_details(request):
    employees = Employee.objects.all()
    print('8888888', employees)
    context = {'employees': employees}
    return render(request, 'employee/employee_detail.html', context)


# emoplyee add update

# product addd
# update
# delete
