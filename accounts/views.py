from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from datetime import timedelta
from .forms import RegisterForm, LoginForm
from main.models import RepairRequest


def register_view(request):
    """
    Регистрация нового пользователя
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('profile')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """
    Вход в систему
    """
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'С возвращением, {user.username}!')
                next_url = request.GET.get('next', 'profile')
                return redirect(next_url)
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """
    Выход из системы
    """
    logout(request)
    messages.info(request, 'Вы вышли из системы.')
    return redirect('home')


@login_required
def profile_view(request):
    """
    Личный кабинет пользователя с пагинацией и фильтрацией
    """
    # Базовый запрос - заявки только текущего пользователя
    user_requests = RepairRequest.objects.filter(user=request.user)

    # ========== ФИЛЬТРАЦИЯ ПО СТАТУСУ ==========
    status_filter = request.GET.get('status', 'all')
    if status_filter and status_filter != 'all':
        user_requests = user_requests.filter(status=status_filter)

    # ========== ФИЛЬТРАЦИЯ ПО ДАТЕ ==========
    date_filter = request.GET.get('date', 'all')
    today = timezone.now().date()

    if date_filter == 'week':
        week_ago = today - timedelta(days=7)
        user_requests = user_requests.filter(created_at__date__gte=week_ago)
    elif date_filter == 'month':
        month_ago = today - timedelta(days=30)
        user_requests = user_requests.filter(created_at__date__gte=month_ago)
    # 'all' - без фильтрации по дате

    # Сортировка по убыванию даты (сначала новые)
    user_requests = user_requests.order_by('-created_at')

    # ========== ПАГИНАЦИЯ (5 заявок на страницу) ==========
    paginator = Paginator(user_requests, 5)
    page = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    # ========== СТАТИСТИКА (для текущих фильтров) ==========
    total_requests = user_requests.count()
    new_requests = user_requests.filter(status='new').count() if total_requests > 0 else 0
    in_progress_requests = user_requests.filter(status='in_progress').count() if total_requests > 0 else 0
    completed_requests = user_requests.filter(status='completed').count() if total_requests > 0 else 0

    # ========== ОБРАБОТКА POST-ЗАПРОСА ДЛЯ РЕДАКТИРОВАНИЯ ПРОФИЛЯ ==========
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.phone = request.POST.get('phone', '')
        user.company = request.POST.get('company', '')
        user.position = request.POST.get('position', '')

        if request.FILES.get('avatar'):
            if user.avatar:
                user.avatar.delete(save=False)
            user.avatar = request.FILES['avatar']

        user.save()
        messages.success(request, 'Профиль успешно обновлён!')
        return redirect('profile')

    context = {
        'user': request.user,
        'page_obj': page_obj,  # объект пагинации (вместо requests)
        'total_requests': total_requests,
        'new_requests': new_requests,
        'in_progress_requests': in_progress_requests,
        'completed_requests': completed_requests,
        'current_status': status_filter,  # для подсветки активного фильтра
        'current_date': date_filter,  # для подсветки активного фильтра даты
    }
    return render(request, 'accounts/profile.html', context)