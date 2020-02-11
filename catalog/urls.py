from django.urls import path
from . import views


'''
The path() below function also specifies a name parameter, which is a 
unique identifier for this particular URL mapping. You can use the 
name to dynamically create a URL that points to the resource that the 
mapper is designed to handle. For example, we can use the name parameter 
to link to our home page from any other page by adding the following link 
in a template: <a href="{% url 'index' %}">Home</a>
'''

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
