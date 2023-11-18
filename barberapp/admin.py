from django.contrib import admin
from django.utils.html import mark_safe

from barberapp.models import Article, Category, Master, Service, Appointment


# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'display_image', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')

    def display_image(self, obj):
        # Здесь вы можете создать HTML-код для отображения изображения
        if obj.images:
            return mark_safe(f'<img src="{obj.images.url}" width="50" height="50" />')
        else:
            return 'Нет изображения'

    display_image.short_description = 'Изображение'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('master_name', 'category', 'description', 'display_image', 'rating')

    def display_image(self, obj):
        # Здесь вы можете создать HTML-код для отображения изображения
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50" height="50" />')
        else:
            return 'Нет изображения'

    display_image.short_description = 'Изображение'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'category', 'price')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('master', 'service', 'date', 'time')