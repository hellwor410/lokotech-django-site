python
from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("✅ Сайт ЛокоТех-Сервис работает!")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
]
