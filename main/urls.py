from django.urls import path

import users
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('second_part', views.second_part, name='second_part'),
    path('about', views.about, name='about'),
    path('government', views.government, name='government'),
    path('faq', views.faq, name='faq'),
    path('entrance_user', views.entrance_user, name='entrance_user'),
    path('entrance_administration', views.entrance_administration, name='entrance_administration'),
    # path('registration_user', views.registration_user, name='registration_user'),
    # path('registration_administration', views.registration_administration, name='registration_administration'),

]
