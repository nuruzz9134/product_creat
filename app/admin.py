from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(ProductMainModel)
class ProductMainModeladmin(admin.ModelAdmin):
    list_display = [
        field.name for field in ProductMainModel._meta.fields
        ]

@admin.register(ProductColourModel)
class ProductColourModeladmin(admin.ModelAdmin):
    list_display = [
        field.name for field in ProductColourModel._meta.fields
        ]

@admin.register(ProductImageModel)
class ProductImageModeladmin(admin.ModelAdmin):
    list_display = [
        field.name for field in ProductImageModel._meta.fields
        ]
