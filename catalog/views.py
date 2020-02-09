from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic  # used to implement a class-based view


class BookListView(generic.ListView):
    """ 
    Used to implement a page listing all books.
    The generic view will query the database to get all records 
    for the specified model (Book).
    """
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author


def index(request):
    """ 
    View function for the home page of the site. 
    """

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    # Count for the number of genres
    genre_instances = Genre.objects.all().count()

    # The number of books with a title including the word 'japan'
    japan_books_available = Book.objects.filter(title__icontains='japan').count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'genre_instances': genre_instances,
        'japan_books_available': japan_books_available,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

