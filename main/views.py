from django.http import HttpResponse

def home(request):
    return HttpResponse("Главная страница из main")

def about(request):
    return HttpResponse("Страница о компании")

def contacts(request):
    return HttpResponse("Контакты")
