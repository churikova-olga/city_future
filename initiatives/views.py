from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from graph.models import Graph
from initiatives.models import Initiative
from django.http import HttpResponse, Http404, HttpResponseRedirect


# голосуют только зарегестрированные пользователи проверить (зарегестрирован ли пользователь)
# при нажатии кнопки рейтинг возрастает на 1 +
# пользователь проголосовал, нельзя больше голосовать
from users.models import UserProfile


def list(request): # добавить initiative_id
    list_id = Initiative.objects.get(id=2) # пример на второй инициативе (должна быть определенная)
    return render(request, 'list.html', {'database_list': list_id})

def detail(request, initiative_id):
    try:
        list_initiative = Initiative.objects.get(id=initiative_id)  # пример на второй инициативе (должна быть определенная)
        if request.method == "POST":
            list_initiative.rating += 1
            list_initiative.save()
    except:
        raise Http404("Инициатива не найдена")

    latest_comment_list = list_initiative.comment_set.order_by('id')
    return render(request, 'initiative.html', {'list_initiative': list_initiative, 'latest_comment_list': latest_comment_list})

def leave_comment(request, initiative_id):

    try:
        list_initiative = Initiative.objects.get(id=initiative_id)

    except:
        raise Http404("Инициатива не найдена")

    list_initiative.comment_set.create(user_comment=UserProfile.objects.get(id=2), message_comment=request.POST['text'])
    return HttpResponseRedirect(reverse('initiatives:detail', args=(list_initiative.id,)))