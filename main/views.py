from django.shortcuts import render
from graph.models import Graph

def index(request):
    return render(request, 'main/index.html')


def search(request):
    a = Graph()
    nodes, edges = a.graph_dict()
    return render(request, 'main/search.html')


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


