"""shoppingmall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.BoardsTemplate.as_view(), name='index'),
    path('detail/<int:pk>', views.BoardsDetail.as_view(), name='boards_detail'),
    path('insert/', views.BoardsInsert.as_view(), name='boards_insert'),
    path('update/<int:pk>', views.BoardsUpdate.as_view(), name='boards_update'),
    path('delete/<int:pk>', views.BoardsDelete.as_view(), name='boards_delete'),
]
