from django.urls import path, include
from . import views
app_name = 'member'
urlpatterns = [
    # path('url패턴', 수행할 함수 또는 클래스, name = 이름),
    path('', views.index, name='index'), # http://localhost:8000/member:insert
    path('insert/', views.insert, name='insert2'),
    path('list/', views.list, name='list2'),
    path('<int:member_id>/', views.detail, name='detail'),
    path('<int:member_id>/delete/', views.delete, name='delete'),
    path('<int:member_id>/update/', views.update, name='update'),
]
