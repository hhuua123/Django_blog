import django.conf.urls
from . import views

app_name = 'defaults'
urlpatterns = [

]

django.conf.urls.handler403 = views.defaults_403
django.conf.urls.handler400 = views.defaults_400
django.conf.urls.handler404 = views.defaults_404
django.conf.urls.handler500 = views.defaults_500