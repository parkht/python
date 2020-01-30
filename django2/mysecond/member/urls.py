from django.urls import path, include
from . import views

urlpatterns = [
    # path('url패턴', 수행할 함수 또는 클래스, name = 이름),
    path('', views.index, name='index'), # http://localhost:8000/member
    path('insert/', views.insert, name='insert'),
    path('list/', views.list, name='list'),
    path('<int:member_id>/', views.detail, name='detail'),
]
