from .models import Category
from .forms import bookSearchForm

def category_links(request):
    categories = Category.objects.all()

    return {'categories': categories}

def searchForm(request):
    search = bookSearchForm

    if request.method == 'POST':
        search = bookSearchForm(request.POST)
        if search.is_valid():
            search.save()

    return {'search': search}
