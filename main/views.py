from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1 style="color:#E30613;">ЛокоТех-Сервис</h1>
        <p>Сайт восстановлен. Следующий шаг — форма заявок.</p>
    """)

def about(request):
    return HttpResponse("<h1>О компании</h1><p>ЛокоТех-Сервис — ремонт локомотивов.</p>")

def contacts(request):
    return HttpResponse("<h1>Контакты</h1><p>service@lokotech.ru | 8-800-555-ЛОКО</p>")
