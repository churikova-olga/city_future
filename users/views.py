from django.http import HttpResponse
from django.shortcuts import render
from .models import UserProfile
# Create your views here.


def register(request):

    return render(request, 'register.html')

def register_form(request):
    res = request.POST
    UserProfile.objects.create(first_name=res['FirstName'], last_name=res['LastName'],
                               address=res['Address'], mobile=res['Mobile'], password=res['Password'], email=res['Email'])

    return HttpResponse('Пользователь успешно зарегистрирован!')

def login_page(request):
    return render(request, 'login.html')


def user(request):
    res = request.POST
    if UserProfile.objects.filter(email=res['Email'], password=res['Password']).exists():
        return HttpResponse(f'Hello, {UserProfile.objects.get(email=res["Email"]).first_name}!')   # redirect
    else:
        return HttpResponse('Пользователь не найден!')