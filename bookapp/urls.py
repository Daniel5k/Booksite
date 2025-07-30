from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('book_detail/<slug:slug>', views.book_detail, name = 'book_detail'),
    path('all_books', views.all_books, name = 'all_books'),
    path('genre/<str:slug>', views.category_detail, name = 'category_detail'),
    path('search_page', views.search_book, name = 'search_book'),
    path('register_page', views.register_page, name = 'register_page'),
    path('login', views.login_page, name = 'login'),
    path('logout', views.logout_page, name = 'logout'),
]