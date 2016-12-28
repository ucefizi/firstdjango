from django.conf.urls import url, include
from django.contrib import admin
from firstapp import urls as firstapp_urls
from charts import urls as charts_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^firstapp/', include(firstapp_urls)),
    url(r'^charts/simple', include(charts_urls)),
]
