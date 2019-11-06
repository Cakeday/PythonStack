from django.conf.urls import url
from . import views

print('ya boi is inside urls.py on the app level RandomWord')
urlpatterns = [
    url(r'^random_word$', views.index),
    url(r'^generate$', views.generator),
    url(r'^clear$', views.clear),

]