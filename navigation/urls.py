from django.conf.urls import url
from django.urls import include

from . import views as core_views
from . import views

urlpattern = [
    url(r'^$', views.index),
]