from django.db import models
from django.urls import reverse

class Member(models.Model):
    """Model representing a team member"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Email unique constraint is used to prevent duplicate member creation
    email = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=100)
    ROLE_TYPE = (
        ('r', 'Regular'),
        ('a', 'Admin')
    )
    status = models.CharField(
        max_length=1,
        choices=ROLE_TYPE,
        blank=True,
        default='r',
        help_text='Role of this team member',
    )

    def __str__(self):
        return self.first_name
    
    def get_id(self):
        return self.id

    def get_absolute_url(self):
        """Returns the specific db row URL for this member."""
        return reverse(args=[str(self.id)])

