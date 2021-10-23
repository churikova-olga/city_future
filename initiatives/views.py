from django.shortcuts import render

# Create your views here.
from graph.models import Graph
from initiatives.models import Initiative
from django.http import HttpResponse

# голосуют только зарегестрированные пользователи проверить (зарегестрирован ли пользователь)
# при нажатии кнопки рейтинг возрастает на 1 +
# пользователь проголосовал, нельзя больше голосовать



def list(request):
    list_initiative = Initiative.objects.get(pk=2) # пример на второй инициативе (должна быть определенная)
    if request.method == "POST":
        list_initiative.rating += 1
        list_initiative.save()
    return render(request, 'list.html', {'list_initiative':list_initiative})