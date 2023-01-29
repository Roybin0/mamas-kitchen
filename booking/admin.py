from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('name', 'customer_email', 'party_size', 'date_time',
                    'special_occasion', 'special_requirements', 'confirmed')
    search_fields = ('name', 'confirm', 'customer_email')
    list_filter = ('name', 'party_size')
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        queryset.update(confirmed=True)
