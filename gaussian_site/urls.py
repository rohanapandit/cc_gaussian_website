"""porject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing'),        # Page 1
    path('login/', views.login_page, name='login_page'), # Page 2
    path('policy/', views.policy_page, name='policy'),   # Page 3
    path('downloads/', views.downloads_page, name='downloads'),
    path('login2/', views.login2, name='login2'),
    path('logout2/', views.logout2, name='logout2'),
    path('auth/', views.auth, name='auth'),   
]