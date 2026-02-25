from django.contrib import admin
from django.contrib.admin import ModelAdmin

from shared.models import Tags, Blogs, Banner






@admin.register(Tags)
class TagsAdmin(ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']


@admin.register(Blogs)
class BlogsAdmin(ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']

@admin.register(Banner)
class BannerAdmin(ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']


