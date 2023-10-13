"""
URL configuration for Bacchos project.

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
from bacchosApp import views
from bacchosApp.views import renderTemplate1
from bacchosApp.views import renderTemplate2
from bacchosApp.views import infoUsuario
from bacchosApp.views import plantilla
from bacchosApp.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/", views.display),
    path('now/', views.displayDateTime),
    path('render1/', renderTemplate1),
    path('render2/', renderTemplate2),
    path('info/', infoUsuario),
    path('plantilla/',plantilla),
    path('index/',index ),
]

