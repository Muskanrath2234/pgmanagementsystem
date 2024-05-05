from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    address = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name

from django.contrib.auth.models import User

class Leave(models.Model):
    """
    Model to store information about leave requests.
    """
    # Model fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    reason = models.TextField()
    room_number = models.CharField(max_length=50)
    bed_number = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()


    # Define choices for status field
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('denied', 'Denied'),
    ]

    # Status field using choices
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    DUE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    due = models.CharField(max_length=3, choices=DUE_CHOICES, default='no')

    def __str__(self):
        return f"Leave Request by {self.user.username}"
