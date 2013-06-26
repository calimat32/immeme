from django.conf.urls import patterns, url

from creator import views

urlpatterns = patterns('',
    url(r'^new/(?P<meme_id>\d+)/$', views.create, name='create'),
    url(r'^$', views.home, name='home')
)
