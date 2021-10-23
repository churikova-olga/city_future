from django.urls import path

from . import views

app_name = 'initiatives'
urlpatterns = [
    #path('index/', views.index, name='list'),
    path('list', views.list, name='list_initiative')
]