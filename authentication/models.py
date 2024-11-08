from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    ROLE_CHOICES = [
        ('organizer', 'Organizer'),
        ('assistant', 'Assistant'),
        ('company', 'Company')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, blank=True, null=True)
    interests = models.TextField(blank=True, help_text="Separate interests by commas, e.g., Python, AI, Data Science")

    def __str__(self):
        return f"{self.user.username}'s Profile"