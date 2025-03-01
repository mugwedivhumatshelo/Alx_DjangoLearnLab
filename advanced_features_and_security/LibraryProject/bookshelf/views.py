from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect

@permission_required('bookshelf.can_view', raise_exception=True)
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book_detail.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Create book logic
        return redirect('book_list')
    return render(request, 'create_book.html')

from django.db.models import Q
from django.forms import Form, CharField
from django.http import HttpResponse
from django.shortcuts import render, redirect

class SearchForm(Form):
    query = CharField()

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Use parameterized query to prevent SQL injection
            results = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
            return render(request, 'search_results.html', {'results': results})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})


