from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request,user)
            return redirect('/')
        else:
            context = {
            'form':form,
            'error':'Ingrese los datos correctamente'
            }
            return render(request, 'register.html', context)
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'register.html', context)

def home(request):
    return render(request, 'home.html')

@login_required
def signout(request):
    logout(request)
    return redirect('inventario')