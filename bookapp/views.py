from django.shortcuts import render, redirect
from .models import Book, Category
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    recommended_books = Book.objects.filter(recommended_books = True)
    fiction_books = Book.objects.filter(fiction_books = True)
    business_books = Book.objects.filter(business_books = True)
    return render(request, 'home.html', {'recommended_books': recommended_books, 
                                         'fiction_books' : fiction_books,
                                         'business_books': business_books,  
})



def details(request, id):
    mybooks = Book.objects.get(id = id)
    template = loader.get_template('book_details.html')
    context = {
        'mybooks' : mybooks,
    }
    return HttpResponse(template.render(context, request))

def all_books(request):
    all_books = Book.objects.all()
    template = loader.get_template('all_books.html')
    context = {
        'all_books' : all_books
    }
    return HttpResponse(template.render(context, request))

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'category': category
    }
    return render(request, 'genre_detail.html', context)
@login_required(login_url='login')
def book_detail(request,slug):
    books = Book.objects.get(slug=slug)
    book_category = books.category.first() 
    similar_books = Book.objects.filter(category__name__startswith = book_category)
    context = {
        'books': books,
        'similar_books': similar_books,
    }
    return render(request, 'book_detail.html', context)

def search_book(request):
    searched_books = Book.objects.filter(title__icontains = request.POST.get('name_of_book'))
    context = {
        'searched_books': searched_books
    }
    return render(request, 'search_book.html', context)

def register_page(request):
    registerForm = CreateUserForm()

    if request.method == 'POST':
        registerForm = CreateUserForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            messages.info(request, 'Account Created Successfully')
            return redirect('login')
       
   

    return render(request, 'register_page.html', {
        'registerForm' :registerForm
    })

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials!!!')

    context = {

    }
    return render(request, 'loginpage.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')
    context = {

    }
    return render(request, 'logout_page.html', context)