from django.urls import path
from .import views
app_name = 'books'

urlpatterns = [
    path('publisher/', views.PublisherList.as_view(), name='publisher_list'),
    path('author/', views.AuthorList.as_view(), name='author_list'),
    path('book/', views.BookList.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisher_detail'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('author/insert/', views.AuthorCreate.as_view(), name='author_insert')
]
# path('', views.클래스명.as_view(), name='')
# 진입메소드 : as_view(), urls.py