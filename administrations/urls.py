from django.urls import path

from . import views

app_name = 'administrations'
urlpatterns = [
    path('', views.statistics.as_view(), name='statistics'),

]