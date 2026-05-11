from django import forms
from .models import RepairRequest


class RepairRequestForm(forms.ModelForm):
    class Meta:
        model = RepairRequest

        fields = [
            'full_name',
            'phone',
            'email',
            'company',
            'locomotive_type',
            'locomotive_model',
            'locomotive_number',
            'repair_type',
            'problem_description',
            'urgent',
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Иванов Иван Иванович'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7 (999) 123-45-67'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@lokotech.ru'
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ООО "РЖД", депо Лесозаводск'
            }),
            'locomotive_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'locomotive_model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2ЭС6, ТЭМ18ДМ'
            }),
            'locomotive_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '001'
            }),
            'repair_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'problem_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Подробно опишите проблему...'
            }),
            'urgent': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }