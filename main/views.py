from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("ЛокоТех-Сервис работает на Vercel!")

def about(request):
    return HttpResponse("О компании")

def contacts(request):
    return HttpResponse("Контакты")
