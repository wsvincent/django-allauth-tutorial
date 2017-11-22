from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
]
