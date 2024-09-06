from django.db import models
from django.contrib.auth.models import AbstractUser

from source.webapp.models import Category, VehicleInfo


# Модель запчастей
class Part(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="parts")  # категория запчасти
    vehicle_info = models.ForeignKey(VehicleInfo, on_delete=models.CASCADE,
                                     related_name="parts")  # информация о транспортном средстве
    name = models.CharField(max_length=255)  # название запчасти
    description = models.TextField()  # описание запчасти
    price = models.DecimalField(max_digits=10, decimal_places=2)  # цена

    def __str__(self):
        return f"{self.name} for {self.vehicle_info.model.brand.name} {self.vehicle_info.model.name}"
