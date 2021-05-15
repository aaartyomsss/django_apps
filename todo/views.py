from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, reverse
from todo.forms.RegistrationForm import RegistrationForm
from todo.forms.LoginForm import LoginForm


def home(request):
    return render(request, 'todo/index.html')


def login_req(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo:index')
    form = LoginForm()
    return render(request, 'todo/login.html', {'form': form})


def registration_req(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('todo:index'))
    else:
        form = RegistrationForm()
    return render(request, 'todo/registration.html', {'form': form})


def logout_req(request):
    logout(request)
    return redirect('todo:index')