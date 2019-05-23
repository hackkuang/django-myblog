from django.contrib import admin

# Register your models here.

from apps.blog.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__all__']
    list_per_page = 10
    list_display_links = ['id', 'code']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['__all__']
    list_per_page = 10
    list_display_links = ['id', 'code']


@admin.register(Recom)
class RecomAdmin(admin.ModelAdmin):
    list_display = ['__all__']
    list_per_page = 10
    list_display_links = ['id', 'code']


@admin.register(Artical)
class ArticalAdmin(admin.ModelAdmin):
    list_display = ['__all__']
    list_per_page = 10
    list_display_links = ['id', 'title']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['__all__']
    list_per_page = 10
    list_display_links = ['id', 'text_info']


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['__all__']
    list_per_page = 10
    list_display_links = ['id', 'name']

