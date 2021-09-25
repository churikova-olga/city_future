from django.urls import path

import administrations.views
from . import views

urlpatterns = [
    path('', administrations.views.sort_rating, name='index'),
    #path('<int:initiative_id>', administrations.views.detail, name='detail')

]