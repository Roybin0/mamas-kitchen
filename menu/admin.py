from django.contrib import admin
from .models import Main, Dessert
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Main)
class MainsMenuAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'description', 'added')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('added', 'title')
    summernote_fields = ('description')


@admin.register(Dessert)
class DessertMenuAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'description', 'added')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('added', 'title')
    summernote_fields = ('description')
