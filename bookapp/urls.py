from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('book_detail/<slug:slug>', views.book_detail, name = 'book_detail'),
    path('all_books', views.all_books, name = 'all_books'),
    path('genre/<str:slug>', views.category_detail, name = 'category_detail'),
]