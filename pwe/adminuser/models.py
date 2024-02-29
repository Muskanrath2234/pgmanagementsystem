from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.urls import reverse

class Profile(models.Model):
    PROF_CHOICES = [
        ('Student', 'Student'),
        ('Job', 'Job'),
        ('Other', 'Other'),
    ]

    WORK_LOC_CHOICES = [
        ('College', 'College'),
        ('Coaching', 'Coaching'),
        ('Office', 'Office'),
        ('Other', 'Other'),
    ]


        # Other fields...

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField( max_length=200, null=True)
    profile_img = models.ImageField(default='image/defalut.jpg',upload_to='media')
    address = models.CharField(max_length=250)
    profession = models.CharField(max_length=100, choices=PROF_CHOICES)
    assosiat_with = models.CharField(max_length=250, blank=True, null=True, choices=WORK_LOC_CHOICES)
    college_name = models.CharField(max_length=250, blank=True, null=True)
    coaching_name = models.CharField(max_length=250, blank=True, null=True)
    office_name = models.CharField(max_length=250, blank=True, null=True)
    other = models.CharField(max_length=250, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    adhar_card = models.ImageField(upload_to='adhar_card/', blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    father_contact_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_joing = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            # Define your maximum image size here
            max_width = 400
            max_height = 200

            if img.width > max_width or img.height > max_height:
                output_size = (max_width, max_height)
                img.thumbnail(output_size)
                img.save(self.image.path)