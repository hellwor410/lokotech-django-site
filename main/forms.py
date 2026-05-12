from django import forms
from .models import RepairRequest

class RepairRequestForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        fields = [
            'full_name', 'phone', 'email', 'company',
            'locomotive_type', 'locomotive_model', 'locomotive_number',
            'repair_type', 'problem_description', 'urgent'
        ]
