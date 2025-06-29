from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)


class Product(models.Model):  # Capitalize model names by convention
    pass


class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=100)

    def __str__(self):
        return self.car_name


# ✅ SIGNAL: Post-save for Car
@receiver(post_save, sender=Car)  # Use @receiver decorator properly
def call_car_api(sender, instance, **kwargs):  # Function name corrected and colon added
    print("CAR OBJECT CREATED")
    print("Sender:", sender)
    print("Instance:", instance)
    print("Kwargs:", kwargs)
