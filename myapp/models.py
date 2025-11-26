from django.db import models

class APIToken(models.Model):
    name = models.CharField(max_length=100)
    token = models.TextField()
    usage_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.usage_count} uses)"
