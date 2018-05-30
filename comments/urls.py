from django.urls import path, re_path
from blogproject.settings import BASE_DIR

from . import views

app_name = 'comments'
urlpatterns = [
    re_path(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]
print(BASE_DIR)