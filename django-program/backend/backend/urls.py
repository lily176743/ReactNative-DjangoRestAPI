"""backend URL Configuration

The `urlpatterns` list routes URLs to views.
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
from django.urls import path, include
from django.conf.urls import url
from  api import views

""" Url Patterns to access others apps """
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'restapi/', include('restapi.urls')),
    path('api/', include('api.urls')), 
    path('faq/', include('api.urls')), 
]
