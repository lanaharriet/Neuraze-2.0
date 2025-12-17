from django.db import models
from django.contrib.auth.models import User


class LearningInsight(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    total_actions = models.IntegerField(default=0)

    library_uses = models.IntegerField(default=0)
    mindgarden_uses = models.IntegerField(default=0)
    whisper_uses = models.IntegerField(default=0)
    crystal_uses = models.IntegerField(default=0)
    community_uses = models.IntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} → {self.total_actions}"
