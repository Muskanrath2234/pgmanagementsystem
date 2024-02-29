from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    address = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name

