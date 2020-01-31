"""myconfig URL Configuration

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
from django.urls import path
from . import views
app_name='polls'
urlpatterns = [
    path('', views.list, name='list'),      # http://localhost:8000/polls/index.html
    path('test/', views.test),  # http://localhost:8000/polls/test/
    path('insert/', views.insert, name='insert'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote')


#    path('insert/', views.insert),  # http://localhost:8000/polls/insert/index.html
]
