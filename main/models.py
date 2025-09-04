from django.db import models

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    service_type = models.CharField(max_length=100, blank=True, null=True)
    budget_range = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)   # ✅ when submitted
    is_read = models.BooleanField(default=False)           # ✅ mark as read/unread

    def __str__(self):
        return f"{self.name} - {self.email}"
