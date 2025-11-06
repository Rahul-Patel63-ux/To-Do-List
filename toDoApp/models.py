from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
# class MyUser(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(null=True, blank=True)
#     password = models.CharField(max_length=255)
#     password2 = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return f"{self.name}"
