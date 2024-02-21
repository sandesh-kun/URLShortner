from django.db import models

# Create your models here.
class UniformResourceLocator(models.Model):
    original_url = models.CharField(null = False, max_length=10000)
    shortened_url = models.CharField(max_length =20, unique = True ) 
    
    def __str__(self):
        return self.original_url
    