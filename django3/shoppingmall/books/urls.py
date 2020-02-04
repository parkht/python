from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.BookTemplate.as_view(), name='index'),
    path('publisher/', views.PublisherList.as_view(), name='publisher_list'),
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisher_detail'),
    path('publisher/insert/', views.PublisherCreate.as_view(), name='publisher_insert'),
    path('publisher/update/<int:pk>', views.PublisherUpdate.as_view(), name='publishser_update'),
    path('publisher/delete/<int:pk>', views.PublisherDelete.as_view(), name='publishser_delete'),
    path('book/', views.BookList.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('author/', views.AuthorList.as_view(), name='author_list'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('author/insert/', views.AuthorCreate.as_view(), name='author_insert'),
    path('author/update/<int:pk>/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/delete/<int:pk>/', views.AuthorDelete.as_view(), name='author_delete'),

]
# path('', views.클래스명.as_view(), name='')
# 진입메소드 : as_view(), urls.py

