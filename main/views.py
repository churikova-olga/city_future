# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from graph.models import Graph


def index(request):
    return render(request, 'main/index.html')


def search(request):
    a = Graph()
    nodes, edges = a.graph_dict() #TODO: починить. Сейчас кавычки и русские буквы кодируются и ломают темплейт.
    return render(request, 'main/search.html', {'nodes': nodes, 'edges': edges})


def create(request):
    return render(request, 'main/create.html')


def second_part(request):
    return render(request, 'main/second_part.html')


def about(request):
    return render(request, 'main/about.html')


def government(request):
    return render(request, 'main/government.html')


def faq(request):
    return render(request, 'main/faq.html')


def entrance_administration(request):
    return render(request, 'main/entrance_administration.html')


def entrance_user(request):
    return render(request, 'main/entrance_user.html')


def registration_user(request):
    return render(request, 'main/registration_user.html')


def registration_administration(request):
    return render(request, 'main/registration_administration.html')


