from django.db import models
from core.models import UserProfile


# Create your models here.
class ScheduledTweet(models.Model):
    content = models.TextField(max_length=280)
    schedule_at = models.DateTimeField()
    is_posted = models.BooleanField(default=False)
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE
    )  # One to many relation (User is the parent )

    class Meta:
        indexes = [
            models.Index(fields=["scheduled_time", "is_posted"]),
        ]
