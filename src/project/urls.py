from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('coming-soon/', include('coming_soon.urls')),
    path('admin/', admin.site.urls),
]
