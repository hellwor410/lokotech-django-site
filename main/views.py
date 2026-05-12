from django.shortcuts import render, redirect
from .forms import RepairRequestForm
from .models import RepairRequest

def home(request):
    if request.method == 'POST':
        form = RepairRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RepairRequestForm()
    return render(request, 'main/home.html', {'form': form})
