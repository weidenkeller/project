from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Главная страница сайта")

def news(request, newsid):
    return HttpResponse(f"<h1>Новости</h1><p>{newsid}</p>")

def about_us(request):
    return  HttpResponse("Список участников клуба")
