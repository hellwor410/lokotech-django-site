from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def temp_home(request):
    return HttpResponse("✅ Vercel + Django 5.1.2 работает!")

urlpatterns = [
    path('', temp_home),  # временная заглушка
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),  # временно на /main/
]
