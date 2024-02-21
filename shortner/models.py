from django.db import models

# Create your models here.
class UniformResourceLocator(models.Model):
    original_url = models.URLField(null = False)
    shortened_url = models.CharField(max_length =20, unique = True ) 
    
    def __str__(self):
        return self.original_url
    