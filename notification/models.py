from django.db import models


class Notification(models.Model):
    message = models.TextField()
    read = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)  # Soft delete flag
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    def mark_as_read(self):
        self.read = True
        self.save()

    def soft_delete(self):
        self.deleted = True
        self.save()
