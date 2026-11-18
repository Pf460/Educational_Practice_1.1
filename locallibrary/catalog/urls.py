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
    re_path(r'^mybooks/$', views.BookInstanceOnLoanView.as_view(), name='my_borrowed'),
    re_path(r'^allborrowed/$', views.ViewAllBookInstancesForLibrarian.as_view(), name='all_borrowed'),
]