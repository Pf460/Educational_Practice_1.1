from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    #__icontains - для поиска подстроки без учёта регистра

    num_genres_western = Genre.objects.filter(name__icontains='western').count()
    num_books_title_book = Book.objects.filter(title__icontains='book').count()

    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genres_western': num_genres_western,
            'num_books_title_book': num_books_title_book
        }
    )