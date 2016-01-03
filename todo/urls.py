from django.conf.urls import include, url
from . import views

app_name = 'todo'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/post_delete/(?P<pk>[0-9]+)/$', views.post_delete, name='post_delete'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]
