from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    teacher_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    completed_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    