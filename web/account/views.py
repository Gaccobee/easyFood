from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import (logout as django_logout,
                                 authenticate,
                                 login as django_login)

from .forms import (loginForm, registerForm)

# LOGIN
# Get username and password from form
# Log user in and redirect to home


def login(request):

    login_form = loginForm()

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            django_login(request, user)
            return redirect('/')
        else:
            print('err')

    return render(request, 'account/login.html', {
        'login_form': login_form
    })


def register(request):

    print('Register view hit!')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username,
                                 email=email,
                                 password=password)
        django_login(request, user)
        return redirect('/')

    register_form = registerForm()

    return render(request, 'account/register.html', {
        'register_form': register_form
    })


def logout(request):

    django_logout(request)

    return HttpResponse(200)
