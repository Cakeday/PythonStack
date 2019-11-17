from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^welcome$', views.welcome),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^add_a_book$', views.add_a_book),
    url(r'^books/(?P<id>\d+)$', views.book_parser),
    url(r'^favorite/(?P<id>\d+)$', views.favorite),
]