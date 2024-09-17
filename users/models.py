from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Customer(AbstractUser):
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name="customuser_set",
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="customuser_set",
        related_query_name="customuser",
    )

    def __str__(self):
        return self.username
