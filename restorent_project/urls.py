"""
URL configuration for restorent_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from Base_App.views import *
from . import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.HomeView, name='HomeView'),      
  path('about', views.AboutView, name='about'),      
  path('menu', views.MenuView, name='menu'),      
  path('Book-Tabel', views.BookTableView, name='Book-Tabel'),      
  path('feedback', views.feedbackView, name='Feedback'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


