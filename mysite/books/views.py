from django.shortcuts import render

# Create your views here. Шаблон интерфейса

from django.http import HttpResponse

def index(request):
    return HttpResponse("All books in our shop")
