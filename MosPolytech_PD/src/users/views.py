from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .forms import UserLoginForm, UserRegistrationForm, AdministrationRegistrationForm
from .models import UserProfile
# Create your views here.



# def register_form(request):
#     res = request.POST
#     UserProfile.objects.create(first_name=res['FirstName'], last_name=res['LastName'],
#                                address=res['Address'], mobile=res['Mobile'], password=res['Password'], email=res['Email'])

    # return HttpResponse('Пользователь успешно зарегистрирован!')
#
# def login_page(request):
#     return render(request, 'login.html')
#
#
# def user(request):
#     res = request.POST
#     if UserProfile.objects.filter(email=res['Email'], password=res['Password']).exists():
#         return HttpResponse(f'Hello, {UserProfile.objects.get(email=res["Email"]).first_name}!')   # redirect
#     else:
#         return HttpResponse('Пользователь не найден!')

def entrance_user(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active and user.is_administration == False:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("search"))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'main/entrance_user.html', context)


def entrance_administration(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active and user.is_administration == True:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("search"))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'main/entrance_administration.html', context)


def registration_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            # rights_users = UserProfile.objects.get(username=request.POST["username"])
            # rights_users.is_administration = False
            # rights_users.save()
            form.save()
            return HttpResponseRedirect(reverse('entrance_user'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'main/registration_user.html', context)


def registration_administration(request):
    if request.method == "POST":
        form = AdministrationRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            # rights_administrations = UserProfile.objects.get(username=request.POST["username"])
            # rights_administrations.is_administration = True
            # rights_administrations.save()
            return HttpResponseRedirect(reverse('entrance_administration'))
        else:
            print(form.errors)
    else:
        form = AdministrationRegistrationForm()
    context = {'form': form}
    return render(request, 'main/registration_administration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('entrance_user'))