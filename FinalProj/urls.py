"""
URL configuration for FinalProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from FinalProjectApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.home, name = "home"),
    path("login/", LoginView.as_view(template_name="FinalProjApp/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("commentpage/", views.commentpage, name="commentpage"),
    path("comment/", views.savecomment, name = "comment"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('studentdetails/', views.studentdetails, name='studentdetails'),
    path('coursedetails/', views.coursedetails, name='coursedetails'),
    path('studentenrollment/', views.studentenrollment, name='studentenrollment'),
    path('save/', views.save, name='save'),

    
]
