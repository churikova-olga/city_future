from django.http import HttpResponse
from django.shortcuts import render
from .models import AdministrationProfile
# Create your views here.


def register_admin(request):

    return render(request, 'register_admin.html')

def register_form_admin(request):
    res = request.POST
    AdministrationProfile.objects.create(first_name=res['FirstName'], last_name=res['LastName'],
                                         address=res['Address'], password=res['Password'], email=res['Email'],
                                         organization=res['Organization'], role=res['Role'], city=res['City'])

    return HttpResponse(f'{AdministrationProfile.objects.get(email=res["Email"]).role} успешно зарегистрирован!')

def login_page_admin(request):
    return render(request, 'login_admin.html')


def administration(request):
    res = request.POST
    if AdministrationProfile.objects.filter(email=res['Email'], password=res['Password']).exists():
        return HttpResponse(f'Hello, {AdministrationProfile.objects.get(email=res["Email"]).role}!')   # redirect
    else:
        return HttpResponse('Пользователь не найден!')