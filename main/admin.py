from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'service_type', 'created_at', 'is_read']
    list_filter = ['service_type', 'is_read', 'created_at']
    search_fields = ['name', 'email', 'company']
    readonly_fields = ['created_at']   # cannot be edited manually
