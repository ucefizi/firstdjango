from django.conf.urls import url
from .views import index, room_detail

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^room/(?P<id>\d+)/', room_detail, name='room_detail'),
]
