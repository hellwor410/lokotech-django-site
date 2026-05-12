from django.db import models

class RepairRequest(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    company = models.CharField(max_length=200)
    locomotive_type = models.CharField(max_length=50, blank=True)
    locomotive_model = models.CharField(max_length=100, blank=True)
    locomotive_number = models.CharField(max_length=50, blank=True)
    repair_type = models.CharField(max_length=50, blank=True)
    problem_description = models.TextField()
    urgent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.company}"
