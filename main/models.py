from django.db import models
from django.conf import settings

class RepairRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    company = models.CharField(max_length=200)
    locomotive_type = models.CharField(max_length=50)
    locomotive_model = models.CharField(max_length=100)
    locomotive_number = models.CharField(max_length=50)
    repair_type = models.CharField(max_length=50)
    problem_description = models.TextField()
    urgent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.locomotive_number}"
