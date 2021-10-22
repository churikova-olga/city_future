from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('second_part', views.second_part, name='second_part'),
    path('about', views.about, name='about'),
    path('government', views.government, name='government'),
    path('faq', views.faq, name='faq'),

]
