from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^interests/$', views.interests, name='interests-index'),
    url(r'^interests/(?P<user_id>\d+)/$', views.show, name='interests-show'),
]
