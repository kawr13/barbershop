from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, time
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Service(models.Model):
    service_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('-price',)  # Делаем сортировку по дате публикации
        indexes = (
            models.Index(fields=['-price']),  # Добавляем индексы для ускорения работы с базой данных
        )

    def __str__(self):
        return self.service_name


class Master(models.Model):
    master_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    photo = models.ImageField(upload_to='masters/masters_photos')
    rating = models.FloatField()

    def __str__(self):
        return self.master_name


class Appointment(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    comments = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def clean(self):
        start_time = time(10, 0)  # 10:00 AM
        end_time = time(20, 0)  # 8:00 PM

        if not (start_time <= self.time <= end_time):
            raise ValidationError("Appointment time must be between 10:00 AM and 8:00 PM.")


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    images = models.ImageField(upload_to='articles/articles_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)  # Делаем сортировку по дате публикации
        indexes = (
            models.Index(fields=['-created_at']),  # Добавляем индексы для ускорения работы с базой данных
        )

    def __str__(self):
        return self.title