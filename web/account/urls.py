from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login, name='account_login'),
    url(r'^register', views.register, name='account_register'),
    url(r'^logout', views.logout, name='account_login'),
]
