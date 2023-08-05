from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image = models.CharField(max_length=1000)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
