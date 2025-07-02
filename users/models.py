import time
from django.db import models
from django.contrib.auth.models import AbstractUser

class Image(models.Model):
    file = models.ImageField(upload_to='carousel_images/')
    description = models.CharField(max_length=128)
    img_id = models.CharField(max_length=8, unique=True)
    date_field = models.DateField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.img_id:
            self.img_id = str(int(time.time() * 1000))[-8:]  
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.description or "Image"

class Carousel(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='carousels')  
    images = models.ManyToManyField('Image', related_name='carousels', blank=True)  
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=64, blank=True, null=True)
    carousel_id = models.CharField(max_length=8, unique=True)
    date_field = models.DateField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.carousel_id:
            self.carousel_id = str(int(time.time() * 1000))[-8:]  
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
class User(AbstractUser):
    fullname = models.CharField(max_length=64)
    nickname = models.CharField(max_length=32, unique=True)
    role = models.CharField(
        max_length=16,
        choices=[
            ('admin', 'Admin'),
            ('normal', 'Normal')
        ],
        default='normal'
    )
    carousel = models.ManyToManyField('Carousel', related_name='owners', blank=True)

    def __str__(self):
        return self.nickname

class AnonymousUser(AbstractUser):
    role = models.CharField(
        max_length=16,
        choices=[('anonymous', 'Anonymous')],
        default='anonymous'
    )

    def __str__(self):
        return self.role