from django.db import models

class Form(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("draft", "Draft"), ("published", "Published"), ("closed", "Closed")], default="draft")
    submissions = models.IntegerField(default=0)
    created_date = models.DateField(null=True, blank=True)
    share_url = models.URLField(blank=True, default="")
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class FormField(models.Model):
    form_title = models.CharField(max_length=255)
    label = models.CharField(max_length=255, blank=True, default="")
    field_type = models.CharField(max_length=50, choices=[("text", "Text"), ("email", "Email"), ("number", "Number"), ("date", "Date"), ("select", "Select"), ("checkbox", "Checkbox"), ("file", "File")], default="text")
    required = models.BooleanField(default=False)
    position = models.IntegerField(default=0)
    placeholder = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.form_title

class Submission(models.Model):
    form_title = models.CharField(max_length=255)
    respondent_email = models.EmailField(blank=True, default="")
    submitted_date = models.DateField(null=True, blank=True)
    ip_address = models.CharField(max_length=255, blank=True, default="")
    data_preview = models.TextField(blank=True, default="")
    status = models.CharField(max_length=50, choices=[("new", "New"), ("reviewed", "Reviewed"), ("archived", "Archived")], default="new")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.form_title
