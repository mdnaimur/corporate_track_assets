from django.shortcuts import render, redirect
from django.http.response import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import MyUserFrom, Products_Form, Employee_Form
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
            return redirect('employee_details')
        else:
            messages.error(
                request, 'An error occured during employee registration"')

    context = {"form": form}
    return render(request, 'employee/employee_add.html', context)


@login_required(login_url='/login')
def employee_details(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employee/employee_detail.html', context)


# emoplyee add update

# product addd
@login_required(login_url='/login')
def add_product(request):
    form = Products_Form()
    if request.method == 'POST':
        form = Products_Form(request.POST)
        messages.error(request, form.errors)

        if form.is_valid():
            product = Product_Assets.objects.create(
                user_host=request.user,
                # employee_user=None,
                product_name=request.POST.get('product_name'),
                # given_date=None,
                # return_date=None,
                # stock=True
            )
            return redirect('home')
        else:
            messages.error(
                request, 'An error occured during employee registration')

    context = {"form": form}
    return render(request, 'product/add_product.html', context)


# Detail Product
@login_required(login_url='/login')
def product_detail(request):
    products = Product_Assets.objects.all()
    context = {'products': products}
    return render(request, 'product/product_view.html', context)


# update Product
@login_required(login_url='/login')
def product_update(request, pk):
    product = Product_Assets.objects.get(id=pk)
    form = Products_Form(instance=product)
    if request.user != product.user_host:
        return HttpResponse('You are not allowed here.....')

    if request.method == 'POST':
        form = Products_Form(request.POST, instance=product)
        form.save()
        return redirect('home')
    else:
        messages.error(
            request, 'An error occured during Product updated')

    context = {'form': form}
    return render(request, 'product/product_update.html', context)


# Delete
@login_required(login_url='/login')
def deleteProduct(request, pk):
    product = Product_Assets.objects.get(id=pk)
    if request.user != product.user_host:
        return HttpResponse('You are not allowed here..')

    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'product/delete.html', {'obj': product})
