from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ContactUsView.as_view(), name='coming-soon'),
]
