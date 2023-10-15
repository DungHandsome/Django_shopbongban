from django.contrib import admin
from .models import Category, product
# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    search_fields = ['name']
    save_as = True
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'date']
    list_filter = ['date']
    search_fields = ['name']
    save_as = True

admin.site.register(Category, AdminCategory)
admin.site.register(product, AdminProduct)