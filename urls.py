from django.conf.urls import urls

from . import views

urlpatterns = [
url(r'^$', views.home, name='home'),

]