from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^shows/new$', views.index),
    url(r'^shows/create$', views.create),
    url(r'^shows/(?P<id>\d+)$', views.display),
    url(r'^shows$', views.everything),
    url(r'^shows/(?P<id>\d+)/edit$', views.edit),
    url(r'^shows/edit$', views.update),
    url(r'^shows/(?P<id>\d+)/destroy$', views.destroy),
]