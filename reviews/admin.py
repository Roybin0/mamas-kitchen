from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        'title', 'customer_name', 'customer_email', 'date', 'reply')
    list_filter = ('customer_name', 'date')
    search_fields = ('customer_name', 'customer_email')
    summernote_fields = ('reply')
