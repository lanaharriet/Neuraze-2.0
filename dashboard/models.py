from django.db import models
from django.contrib.auth.models import User

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feature = models.CharField(max_length=100)
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
