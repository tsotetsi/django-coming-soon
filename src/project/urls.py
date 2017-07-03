from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^coming-soon/', include('coming_soon.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
