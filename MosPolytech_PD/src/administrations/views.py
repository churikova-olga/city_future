from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from initiatives.models import Initiative
from .models import Statistics
# Create your views here.


# def register_admin(request):
#
#     return render(request, 'register_admin.html')

class statistics(TemplateView):

    template_name = 'admin_statistics.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Initiative.objects.all()
        return context
#
#
# def administration(request):
#     res = request.POST
#     if AdministrationProfile.objects.filter(email=res['Email'], password=res['Password']).exists():
#         return HttpResponse(f'Hello, {AdministrationProfile.objects.get(email=res["Email"]).role}!')   # redirect
#     else:
#         return HttpResponse('Пользователь не найден!')