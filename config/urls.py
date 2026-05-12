from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("✅ Vercel + Django 5.1.2 работает!")

urlpatterns = [
    path('', home),
]
