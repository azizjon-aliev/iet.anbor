from dataclasses import fields
from distutils.ccompiler import show_compilers
from django.contrib import admin
from .models import Category, Product, Counterparty, Operation, OperationGroup
from django.utils.html import format_html


class BaseModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(BaseModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(BaseModelAdmin):
    list_display = ('show_image', 'title', 'category', 'created_at',)
    autocomplete_fields = ('category',)
    search_fields = ('title', 'category__name',)
    list_filter = ('category',)
    fields = (
        'show_image',
        'image',
        'title',
        'description',
        'category',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'show_image',
        'created_at',
        'updated_at',
    )

    def show_image(self, obj):
        url = '/static/anbor/img/default_product.png'

        if obj.image:
            url = obj.image.url
            
        return format_html(f"<img src='{url}' width={70} height={70} />")

    show_image.short_description = 'изоброжение'
    

@admin.register(Counterparty)
class CounterpartyAdmin(BaseModelAdmin):
    search_fields = (
        'name', 
        'full_name', 
        'phone_number', 
        'inn',
    )
    list_display = (
        'name', 
        'full_name', 
        'phone_number', 
        'inn',
        'created_at',
    )
    readonly_fields = (
        'created_at', 'updated_at', 
    )


class OperationInline(admin.TabularInline):
    model = Operation
    autocomplete_fields = ('product',)
    extra = 1
    
    
@admin.register(OperationGroup)
class OperationGroupAdmin(BaseModelAdmin):
    autocomplete_fields = ('counterparty',)
    inlines = (OperationInline,)
    readonly_fields = ('created_at', 'updated_at',)
    fields = ('counterparty', 'action', 'comment', 'created_at', 'updated_at',)

    def amount(self, obj):
        return 100