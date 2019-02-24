"""admin_net_model URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from net_model import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', views.Get_Patient_Info),
    path('init/', views.Get_Search_result),
    path('showMessage/', views.Edit_Patient_Ill),
    path('addMessage/', views.Add_Ill_Info),
    path('showDetail/', views.Get_Nodule_Info)
]
