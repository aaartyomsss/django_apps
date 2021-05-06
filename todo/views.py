from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, reverse
from todo.forms.RegistrationForm import RegistrationForm


def home(request):

    return HttpResponse("yes")


def registration(request):
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