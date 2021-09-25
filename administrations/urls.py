from django.urls import path

from . import views

app_name = 'administrations'
urlpatterns = [
    path('', views.register_admin, name='administration'),
    path('administration_form/', views.register_form_admin, name='admin form'),

]