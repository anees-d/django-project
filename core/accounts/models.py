from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager  # ✅ correct import


class CustomUser(AbstractUser):
    username = None  # ❌ remove default username
    email = None     # ❌ optional, remove if not used
    phone_number = models.CharField(max_length=15, unique=True)
    user_bio = models.CharField(max_length=100, blank=True, null=True)
    user_profile_image = models.ImageField(upload_to="profile", blank=True, null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []  # ❗no extra fields required during superuser creation

    objects = CustomUserManager()  # ✅ connect the manager

    def __str__(self):
        return self.phone_number
