from django.contrib import admin
from .models import Category, Model3D

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Model3D)
class Model3DAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'nivel')
    search_fields = ('nombre',)
    list_filter = ('categoria', 'nivel')

