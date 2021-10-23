from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import UserLoginForm, UserRegistrationForm
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

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("index"))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)
