from django.contrib import admin
from .models import Category, Product


class BaseModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(BaseModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(BaseModelAdmin):
    list_display = ('title', 'category', 'created_at',)
    autocomplete_fields = ('category',)
    search_fields = ('title', 'category__name',)
    list_filter = ('category',)