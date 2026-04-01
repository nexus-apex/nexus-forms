from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Form, FormField, Submission
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusForms with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusforms.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Form.objects.count() == 0:
            for i in range(10):
                Form.objects.create(
                    title=f"Sample Form {i+1}",
                    category=f"Sample {i+1}",
                    status=random.choice(["draft", "published", "closed"]),
                    submissions=random.randint(1, 100),
                    created_date=date.today() - timedelta(days=random.randint(0, 90)),
                    share_url=f"https://example.com/{i+1}",
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Form records created'))

        if FormField.objects.count() == 0:
            for i in range(10):
                FormField.objects.create(
                    form_title=f"Sample FormField {i+1}",
                    label=f"Sample {i+1}",
                    field_type=random.choice(["text", "email", "number", "date", "select", "checkbox", "file"]),
                    required=random.choice([True, False]),
                    position=random.randint(1, 100),
                    placeholder=f"Sample {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 FormField records created'))

        if Submission.objects.count() == 0:
            for i in range(10):
                Submission.objects.create(
                    form_title=f"Sample Submission {i+1}",
                    respondent_email=f"demo{i+1}@example.com",
                    submitted_date=date.today() - timedelta(days=random.randint(0, 90)),
                    ip_address=f"Sample {i+1}",
                    data_preview=f"Sample data preview for record {i+1}",
                    status=random.choice(["new", "reviewed", "archived"]),
                )
            self.stdout.write(self.style.SUCCESS('10 Submission records created'))
