from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    # path('register/', views.register, name='register'),
    #path('login/', views.login, name='login')
    path('entrance_user', views.entrance_user, name='entrance_user'),
    path('entrance_administration', views.entrance_administration, name='entrance_administration'),
    path('registration_user', views.registration_user, name='registration_user'),
    path('registration_administration', views.registration_administration, name='registration_administration'),
    path('logout', views.logout, name='logout')
]