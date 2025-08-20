from .models import Category, Book
from .forms import bookSearchForm


def category_links(request):
    categories = Category.objects.all()

    return {'categories': categories}

def BookSearchForm(request):
    searchForm = bookSearchForm

    if request.method == 'POST':
        searchForm = bookSearchForm(request.POST)
        if searchForm.is_valid():
            searchForm.save()
    
    return {'searchForm': searchForm}


