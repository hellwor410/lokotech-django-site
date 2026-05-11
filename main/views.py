from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RepairRequestForm
from .models import RepairRequest
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method == 'POST':

        data = request.POST.copy()


        data['status'] = 'new'


        form = RepairRequestForm(data)

        if form.is_valid():

            repair_request = form.save()


            print(f"✅ ЗАЯВКА СОХРАНЕНА! ID: {repair_request.id}")
            print(f"   Имя: {repair_request.full_name}")
            print(f"   Статус: {repair_request.status}")

            messages.success(
                request,
                f'✅ Заявка #{repair_request.id} успешно отправлена!'
            )
            return redirect('home')
        else:

            print("❌ ОШИБКИ ФОРМЫ:", form.errors)
            messages.error(request, '❌ Пожалуйста, исправьте ошибки в форме.')
    else:
        form = RepairRequestForm()


    total_requests = RepairRequest.objects.count()
    completed_requests = RepairRequest.objects.filter(status='completed').count()

    context = {
        'form': form,
        'total_requests': total_requests,
        'completed_requests': completed_requests,
    }
    return render(request, 'main/home.html', context)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def home(request):
    if request.method == 'POST':
        form = RepairRequestForm(request.POST)
        if form.is_valid():
            repair_request = form.save(commit=False)
            # Если пользователь авторизован, привязываем заявку к нему
            if request.user.is_authenticated:
                repair_request.user = request.user
            repair_request.save()
            messages.success(request, f'✅ Заявка #{repair_request.id} успешно отправлена!')
            return redirect('home')
        else:
            messages.error(request, '❌ Пожалуйста, исправьте ошибки в форме.')
    else:
        form = RepairRequestForm()

    total_requests = RepairRequest.objects.count()
    completed_requests = RepairRequest.objects.filter(status='completed').count()

    context = {
        'form': form,
        'total_requests': total_requests,
        'completed_requests': completed_requests,
    }
    return render(request, 'main/home.html', context)