import django.conf.urls
from . import views
from django.urls import path

app_name = 'defaults'
urlpatterns = [
    path(django.conf.urls.handler403, views.defaults_403),
    path(django.conf.urls.handler400, views.defaults_400),
    path(django.conf.urls.handler404, views.defaults_404),
    path(django.conf.urls.handler500, views.defaults_500),
]

django.conf.urls.handler403 = views.defaults_403
django.conf.urls.handler400 = views.defaults_400
django.conf.urls.handler404 = views.defaults_404
django.conf.urls.handler500 = views.defaults_500
