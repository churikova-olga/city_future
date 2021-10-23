"""basic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import users

import administrations
import users

urlpatterns = [

    path('', include('initiatives.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    # path('page/', users.views.user, name='user_page'),
    # path('login_admin/', administrations.views.login_page_admin, name='login_page_admin'),
    # path('admin_page', administrations.views.administration, name='admin_page'),
    # path('register_admin/', include('administrations.urls')),
    # path('login/', users.views.login_page, name='login_page'),
    # #path('initiatives/', include('initiatives.urls')),
]
