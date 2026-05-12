from django.http import HttpResponse

def home(request):
    return HttpResponse("Главная страница ЛокоТех-Сервис")

def about(request):
    return HttpResponse("О компании: ЛокоТех-Сервис — ремонт локомотивов")

def contacts(request):
    return HttpResponse("Контакты: 8-800-555-ЛОКО | service@lokotech.ru")
