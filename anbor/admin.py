from django.contrib import admin
from .models import Category


class BaseModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(BaseModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    search_fields = ('name',)

