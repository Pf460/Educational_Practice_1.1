from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    #__icontains - для поиска подстроки без учёта регистра

    num_genres_western = Genre.objects.filter(name__icontains='western').count()
    num_books_title_book = Book.objects.filter(title__icontains='book').count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genres_western': num_genres_western,
            'num_books_title_book': num_books_title_book,
            'num_visits': num_visits
        }
    )

class BookListView(generic.ListView):
    model = Book
    pagination_by = 10
    # def get_context_data(self, **kwargs):
    #     получаем основной контекст
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     определение новой переменной в контексте
    #     context['some_data'] = 'This is some date'
    #     return context

    #[:5] сколько мы выводим
    def get_queryset(self):
        return Book.objects.all()[:5]
    template_name = 'books/book_list.html'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def book_detail_view(request, pk):
        try:
            book_id = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")
        # Более простая обработка ошибки 404
        # book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'catalog/book_detail.html',
            context={'book': book_id, }
        )

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10
    template_name = 'authors/author_list.html'

    def get_queryset(self):
        return Author.objects.all()[:5]

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'authors/author_detail.html'

    def author_detail_view(request, pk):
        try:
            author_id = Author.objects.get(pk=pk)
        except:
            raise Http404("Author does not exist")

        return render(
            request,
            'authors/author_detail.html',
            context={'author': author_id, }
        )

class BookInstanceOnLoanView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'bookinstance_list.html'
    pagination_by = 10
    def get_queryset(self):
        return BookInstance.objects.filter(borrower = self.request.user).filter(status__exact="o").order_by('due_back')

class ViewAllBookInstancesForLibrarian(PermissionRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'librarian/allbookinstance_list.html'
    paginate_by = 10
    permission_required = (
        'catalog.can_mark_returned',
        'catalog.can_edit'
    )

    raise_exception = True #настройка обработки прав пользования

    def get_queryset(self):
        return BookInstance.objects.all().order_by('due_back')