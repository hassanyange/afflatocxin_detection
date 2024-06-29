from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
    

class AdminHOD(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Crop(models.Model):
    CROP_CHOICES = [
        ('maize', 'Maize'),
        ('groundnut', 'Groundnut'),
    ]
    name = models.CharField(max_length=50, choices=CROP_CHOICES, unique=True)

    def __str__(self):
        return self.name

class Test(models.Model):
    crop = models.ForeignKey(Crop, related_name='tests', on_delete=models.CASCADE)
    sample_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    gps_location = models.CharField(max_length=100)
    aflatoxin_level = models.DecimalField(max_digits=5, decimal_places=2)
    sample_photo = models.ImageField(upload_to='samples/')

    def __str__(self):
        return f"Test {self.sample_id} for {self.crop.name}"