from django.contrib import admin
from django.contrib.admin import ModelAdmin

from product.models import Author, Category, Product


# Register your models here.


@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    list_display = ('professions',)
    search_fields = ('full_name',)



@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['id', 'title',]
    search_fields = ['title',]

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']
