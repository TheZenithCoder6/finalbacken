from django.db import models

from django.db import models

class Product(models.Model):

    CATEGORY_CHOICES = [
        ("Metal", "Metal"),
        ("Terracotta", "Terracotta"),
        ("Photography", "Photography"),
        ("Glass Art", "Glass Art"),
        ("Premium", "Premium"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.URLField(blank=True, null=True)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Other"
    )

    artist_name = models.CharField(max_length=200, blank=True, null=True)
    dimensions = models.CharField(max_length=100, blank=True, null=True)


    size_inch = models.CharField(max_length=50, blank=True, null=True)
    size_cm = models.CharField(max_length=50, blank=True, null=True)
    medium = models.CharField(max_length=50, blank=True, null=True)
    style = models.CharField(max_length=50, blank=True, null=True)

    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.is_available = self.stock > 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Artist(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    dob = models.CharField(max_length=50)
    image = models.URLField()
    about = models.TextField()

    is_top = models.BooleanField(default=False)  
    short_about = models.CharField(max_length=50)  

    def __str__(self):
        return self.name