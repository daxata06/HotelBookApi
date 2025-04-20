from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=35)

    ROLE_CHOICES = (
        ("User", "User"),
        ("Administrator", "Administrator"),
    )
    role = models.CharField(choices=ROLE_CHOICES)
    email = models.EmailField(
        ("email address"),
        unique=True,
        error_messages={
            "unique": ("A user with that email already exists."),
        },
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
