from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
# from .models import Cuestionario, Asistencia
# from .forms import CuestionarioForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {
            'form':form,
            'error':'Ingrese los datos correctamente'
            }
            context.update(csrf(request))  # include CSRF token
            return render(request, 'registration/register.html', context)
    else:
        form = UserCreationForm()
        context = {'form': form}
        context.update(csrf(request))  # include CSRF token
        return render(request, 'registration/register.html', context)

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            context = {
                'form': form,
                'error': 'Invalid username or password'
            }
            context.update(csrf(request))  # include CSRF token
            return render(request, 'registration/login.html', context)
    else:
        form = LoginForm()
        context = {'form': form}
        context.update(csrf(request))  # include CSRF token
        return render(request, 'registration/login.html', context)


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def signout(request):
    logout(request)
    return redirect('home')

# @login_required
# def cuestionario_list(request):
#     cuestionarios = Cuestionario.objects.all()
#     return render(request, 'cuestionario_list.html', {'cuestionarios': cuestionarios})

# @login_required
# def cuestionario_create(request):
#     if request.method == 'POST':
#         form = CuestionarioForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('cuestionario_list')
#     else:
#         form = CuestionarioForm()
#     return render(request, 'cuestionario_create.html', {'form': form})

# @login_required
# def asistencia_list(request):
#     asistencias = Asistencia.objects.all()
#     return render(request, 'asistencia_list.html', {'asistencias': asistencias})

# def cuestionario_create(request):
#     if request.method == 'POST':
#         form = CuestionarioForm(request.POST)
#         pregunta_formset = PreguntaFormSet(request.POST)
#         if form.is_valid() and pregunta_formset.is_valid():
#             cuestionario = form.save()
#             pregunta_formset.instance = cuestionario
#             pregunta_formset.save()
#             return redirect('cuestionario_list')
#     else:
#         form = CuestionarioForm()
#         pregunta_formset = PreguntaFormSet()
#     return render(request, 'cuestionario_create.html', {'form': form, 'pregunta_formset': pregunta_formset})