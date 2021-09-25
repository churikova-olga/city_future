from django.http import HttpResponse
from django.shortcuts import render
from .models import AdministrationProfile
from initiatives.models import Initiative
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

def sort_rating(request):
    list_initiative = Initiative.objects.order_by('-rating')
    return render(request, 'list.html', {'list_initiative': list_initiative})

def change_status(request):

    #Initiative.objects.get(id=1).status //= "Принята"

    pass



# def detail(request, initiative_id):
#     try:
#         a = Initiative.object.get(id = initiative_id)
#     except:
#

