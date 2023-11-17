from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50)


class Service(models.Model):
    service_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Master(models.Model):
    master_name = models.CharField(max_length=50)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.TextField()
    photo = models.ImageField(upload_to='masters_photos')
    rating = models.FloatField()


class Appointment(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)