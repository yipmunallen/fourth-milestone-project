from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'sku',
        'name',
        'get_category',
        'price',
        'rating',
        'image',
        'image_2'
    )

    def get_category(self, obj):
        return obj.category.friendly_name
    get_category.short_description = 'Category'

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
