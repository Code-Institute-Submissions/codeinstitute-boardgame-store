from django.db import models
from pyuploadcare.dj.models import ImageField

class Game(models.Model):
    name = models.CharField(blank=False, max_length=21)
    description = models.TextField(blank=False)
    inside_box = models.TextField(blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = ImageField(null=True, blank=False)
    
    def __str__(self):
        return "{} ({})".format(self.name, self.category)
        
class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        # return "{} (id: {})".format(self.name, self.id)
        return self.name