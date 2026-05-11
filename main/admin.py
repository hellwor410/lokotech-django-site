from django.contrib import admin
from django.utils.html import format_html
from .models import RepairRequest


@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    """Админ-панель для управления заявками"""

    list_display = (
        'id',
        'status',
        'user',
        'status_colored',
        'full_name',
        'phone',
        'company',
        'locomotive_info',
        'created_at_display',
        'urgent_display',
    )

    list_filter = (
        'status',
        'urgent',
        'locomotive_type',
        'repair_type',
        'created_at',
    )

    search_fields = (
        'full_name',
        'phone',
        'email',
        'company',
        'locomotive_number',
        'locomotive_model',
    )

    list_editable = ('status',)

    readonly_fields = ('created_at', 'updated_at')

    def locomotive_info(self, obj):
        return f"{obj.get_locomotive_type_display()} {obj.locomotive_model} ({obj.locomotive_number})"

    locomotive_info.short_description = 'Локомотив'

    def status_colored(self, obj):
        colors = {
            'new': 'primary',
            'in_progress': 'warning',
            'completed': 'success',
            'cancelled': 'danger',
        }
        return format_html(
            '<span class="badge bg-{}">{}</span>',
            colors.get(obj.status, 'secondary'),
            obj.get_status_display()
        )

    status_colored.short_description = 'Статус'

    def created_at_display(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')

    created_at_display.short_description = 'Создана'

    def urgent_display(self, obj):
        if obj.urgent:
            return format_html('<span class="badge bg-danger">СРОЧНО</span>')
        return ''

    urgent_display.short_description = 'Срочность'

    actions = ['mark_as_in_progress', 'mark_as_completed']

    def mark_as_in_progress(self, request, queryset):
        queryset.update(status='in_progress')
        self.message_user(request, f'{queryset.count()} заявок переведены в статус "В работе"')

    mark_as_in_progress.short_description = 'Отметить как "В работе"'

    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
        self.message_user(request, f'{queryset.count()} заявок отмечены как выполненные')

    mark_as_completed.short_description = 'Отметить как "Выполнено"'