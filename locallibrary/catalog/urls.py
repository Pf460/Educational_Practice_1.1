from django.urls import path
from django.urls import re_path
from . import views

#from django.conf.urls import url - признан устаревшим в версиях Django 4.0 и выше

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^books/$', views.BookListView.as_view(), name='books'),
#     url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
# ]

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book_detail'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author_detail'),
    re_path(r'^genres/$', views.GenreListView.as_view(), name='genres'),
    re_path(r'^genre/(?P<pk>\d+)$', views.GenreDetailView.as_view(), name='genre_detail'),
    re_path(r'^mybooks/$', views.BookInstanceOnLoanView.as_view(), name='my_borrowed'),
    re_path(r'^allborrowed/$', views.ViewAllBookInstancesForLibrarian.as_view(), name='all_borrowed'),
    re_path(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew_book_librarian'),
    re_path(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    re_path(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    re_path(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
    re_path(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    re_path(r'^book/(?P<pk>\d+)/update/$', views.BookUpdate.as_view(), name='book_update'),
    re_path(r'^book/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book_delete'),
    re_path(r'^genre/create/$', views.GenreCreate.as_view(), name='genre_create'),
    re_path(r'^genre/(?P<pk>\d+)/update/$', views.GenreUpdate.as_view(), name='genre_update'),
    re_path(r'^genre/(?P<pk>\d+)/delete/$', views.GenreDelete.as_view(), name='genre_delete'),
]