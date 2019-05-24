from django.contrib import admin

# Register your models here.

from blogapp.models import *

admin.site.site_title = '我的博客'
admin.site.site_header = '汪春旺个人博客后台管理系统'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name']
    list_per_page = 10
    list_display_links = ['id', 'code']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name']
    list_per_page = 10
    list_display_links = ['id', 'code']


@admin.register(Recom)
class RecomAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name']
    list_per_page = 10
    list_display_links = ['id', 'code']


@admin.register(Artical)
class ArticalAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'views', 'create_time']
    list_per_page = 10
    list_display_links = ['id', 'title']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'text_info', 'img', 'link_url', 'is_active']
    list_per_page = 10
    list_display_links = ['id', 'text_info']


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link_url']
    list_per_page = 10
    list_display_links = ['id', 'name']

