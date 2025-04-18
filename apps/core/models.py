from django.db import models

# Core models for the RescueMe application
# This file should be kept minimal as most functionality is in specific apps

class Contact(models.Model):
    """Model for storing contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

# Newsletter store subscribers
        
class Newsletter(models.Model):
    """Model for storing newsletter subscribers"""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Newsletter Subscriber"
        verbose_name_plural = "Newsletter Subscribers"