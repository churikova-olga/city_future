from django.urls import path

from . import views

app_name = 'initiatives'
urlpatterns = [
    #path('index/', views.index, name='list'),
    path('list/', views.list, name='list_initiative'),
    path('list/<int:initiative_id>/', views.detail, name='detail'),
    path('list/<int:initiative_id>/leave_comment/', views.leave_comment, name='leave_comment')
]