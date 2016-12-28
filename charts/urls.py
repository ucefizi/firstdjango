from django.conf.urls import url
from .views import simple

urlpatterns = [
    url(r'^$', simple , name='simple_chart'),
]
