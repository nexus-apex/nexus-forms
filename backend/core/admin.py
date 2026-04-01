from django.contrib import admin
from .models import Form, FormField, Submission

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "status", "submissions", "created_date", "created_at"]
    list_filter = ["status"]
    search_fields = ["title", "category"]

@admin.register(FormField)
class FormFieldAdmin(admin.ModelAdmin):
    list_display = ["form_title", "label", "field_type", "required", "position", "created_at"]
    list_filter = ["field_type"]
    search_fields = ["form_title", "label", "placeholder"]

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ["form_title", "respondent_email", "submitted_date", "ip_address", "status", "created_at"]
    list_filter = ["status"]
    search_fields = ["form_title", "respondent_email", "ip_address"]
