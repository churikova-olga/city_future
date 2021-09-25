from django.http import HttpResponse
from django.shortcuts import render
from .models import UserProfile
# Create your views here.


def register(request):

    return render(request, 'register.html')


def register_form(request):
    res = request.POST
    UserProfile.objects.create(first_name=res['FirstName'], last_name=res['LastName'],
                               address=res['Address'], mobile=res['Mobile'])
    return HttpResponse('Пользователь успешно зарегистрирован!')