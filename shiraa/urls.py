from django.urls import path, include
from django.conf.urls import url, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('blog', views.blog, name='blog'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]