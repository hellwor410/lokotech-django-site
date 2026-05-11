from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Сайт ЛокоТех-Сервис работает! Поздравляю!")

def about(request):
    return HttpResponse("Страница о компании")

def contacts(request):
    return HttpResponse("Контакты")
