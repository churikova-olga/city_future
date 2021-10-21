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
