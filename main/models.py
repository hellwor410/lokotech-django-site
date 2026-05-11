from django.db import models
from django.conf import settings


class RepairRequest(models.Model):
    """
    Модель заявки на ремонт локомотива
    """

    # Типы локомотивов
    LOCOMOTIVE_TYPES = [
        ('electric', 'Электровоз'),
        ('diesel', 'Тепловоз'),
        ('shunter', 'Маневровый локомотив'),
        ('passenger', 'Пассажирский локомотив'),
        ('freight', 'Грузовой локомотив'),
        ('special', 'Спецтехника'),
    ]

    # Виды ремонта
    REPAIR_TYPES = [
        ('diagnostics', 'Техническая диагностика'),
        ('maintenance', 'Техническое обслуживание'),
        ('current', 'Текущий ремонт'),
        ('medium', 'Средний ремонт'),
        ('capital', 'Капитальный ремонт'),
        ('emergency', 'Аварийный ремонт'),
    ]

    # Статусы заявки
    STATUS_CHOICES = [
        ('new', 'Новая заявка'),
        ('in_progress', 'В работе'),
        ('completed', 'Выполнено'),
        ('cancelled', 'Отменена'),
    ]

    # ========== СВЯЗЬ С ПОЛЬЗОВАТЕЛЕМ ==========
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Пользователь',
        help_text='Авторизованный пользователь, создавший заявку'
    )

    # ========== КОНТАКТНЫЕ ДАННЫЕ ==========
    full_name = models.CharField(
        max_length=200,
        verbose_name='ФИО заявителя'
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон'
    )
    email = models.EmailField(
        verbose_name='Email',
        blank=True,
        help_text='Необязательно'
    )
    company = models.CharField(
        max_length=200,
        verbose_name='Предприятие',
        help_text='Название предприятия или депо'
    )

    # ========== ДАННЫЕ О ЛОКОМОТИВЕ ==========
    locomotive_type = models.CharField(
        max_length=50,
        choices=LOCOMOTIVE_TYPES,
        verbose_name='Тип локомотива'
    )
    locomotive_model = models.CharField(
        max_length=100,
        verbose_name='Модель локомотива'
    )
    locomotive_number = models.CharField(
        max_length=50,
        verbose_name='Номер локомотива'
    )

    # ========== ДАННЫЕ О РЕМОНТЕ ==========
    repair_type = models.CharField(
        max_length=50,
        choices=REPAIR_TYPES,
        verbose_name='Вид ремонта'
    )
    problem_description = models.TextField(
        verbose_name='Описание проблемы'
    )

    # ========== ДОПОЛНИТЕЛЬНЫЕ ПОЛЯ ==========
    urgent = models.BooleanField(
        default=False,
        verbose_name='Срочная заявка'
    )

    # ========== СИСТЕМНЫЕ ПОЛЯ ==========
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'Заявка на ремонт'
        verbose_name_plural = 'Заявки на ремонт'
        ordering = ['-created_at']

    def __str__(self):
        return f'Заявка #{self.id} - {self.locomotive_number} ({self.get_repair_type_display()})'