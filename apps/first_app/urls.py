from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),    # This line has changed!
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.success),    # This line has changed!
        # This line has changed!
        # This line has changed!
    ]
