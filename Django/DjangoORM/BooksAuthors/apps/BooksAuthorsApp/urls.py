from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$', views.author_index),
    url(r'^books/(?P<id>\d+)$', views.books),
    url(r'^authors/(?P<id>\d+)$', views.authors),
    url(r'^book_add$', views.book_add),
    url(r'^author_add$', views.author_add),
    url(r'^book_add_from_author$', views.book_add_from_author),
    url(r'^author_add_from_book$', views.author_add_from_book),
]