from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RepairRequest

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        problem = request.POST.get('problem')
        RepairRequest.objects.create(
            name=name,
            phone=phone,
            problem=problem
        )
        return redirect('home')
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')
