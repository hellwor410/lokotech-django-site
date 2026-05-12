from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("✅ Vercel + Django 5.1.2 работает!")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  
]
