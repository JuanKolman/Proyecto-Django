"""
URL configuration for inventario_alpha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
   
   #auth
    path('signin/', views.signin, name='signin'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', success_url='/'), name='login'),
    path('signup/', views.signup, name = 'signup'),
    path('signout/', views.signout, name = 'signout'),
    
    #cuestionario
    # path('cuestionario/', views.cuestionario_list, name='cuestionario_list'),
    # path('cuestionario/create/', views.cuestionario_create, name='cuestionario_create'),
    # path('asistencia/', views.asistencia_list, name='asistencia_list'),
    
]