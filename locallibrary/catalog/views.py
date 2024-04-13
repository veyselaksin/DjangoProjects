from typing import Any
from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
from django.http import Http404

# Create your views here.
def index(request:object):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

    context_object_name = 'book_list'   # your own name for the list as a template variable
    queryset = Book.objects.all() 
    template_name = 'catalog/book_list.html'  # Specify your own template name/location

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(BookListView, self).get_context_data(**kwargs)

        # Add in a QuerySet of all the genres
        context['genre_list'] = Genre.objects.all()

        return context

class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk=primary_key)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")

        return render(request, 'catalog/book_detail.html', context={'book': book})
    
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2

    context_object_name = 'author_list'   # your own name for the list as a template variable
    queryset = Author.objects.all() 
    template_name = 'catalog/author_list.html'  # Specify your own template name/location

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(AuthorListView, self).get_context_data(**kwargs)

        # Add in a QuerySet of all the genres
        context['genre_list'] = Genre.objects.all()

        return context
    
class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request, primary_key):
        try:
            author = Author.objects.get(pk=primary_key)
        except Author.DoesNotExist:
            raise Http404("Author does not exist")

        return render(request, 'catalog/author_detail.html', context={'author': author})
    
