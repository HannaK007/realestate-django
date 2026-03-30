from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


# Create your models here.

class Property(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=12,decimal_places=2)
    location = models.CharField(max_length=200)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    image = CloudinaryField('image', blank=True, null=True)  # <-- CloudinaryField instead of ImageField
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title