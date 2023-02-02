from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^products/$', views.EcommerceAPI),
    re_path(r'^products/([0-9]+)$', views.EcommerceAPI)
]
