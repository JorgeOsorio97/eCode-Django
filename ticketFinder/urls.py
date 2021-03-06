"""AtmClean URL Configuration

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
from django.urls import path, re_path
from ticketFinder import views
from AtmClean import views as vw

app_name = 'ticketFinder'
    
urlpatterns = [    
    path('', views.index, name = 'index'),
    re_path(r'options/$',views.options, name = 'options'),
    re_path(r'ecode/$', views.ecode, name = 'ecode'),
    path('cuestionario/', views.cuestionario, name = 'cuestionario'),
    re_path(r'POST_buscar/$', views.POST_cuestionario, name = 'POST_cuestionario'),
    re_path(r'charts/$', views.charts, name='charts'),
    re_path(r'POST_ecode2tran/$', views.POST_ecode2tran, name='ecode2tran'),
    re_path(r'cuestionario/generatePDF/$', vw.GeneratePDF.as_view(), name = 'genPDFs'),
    
]
