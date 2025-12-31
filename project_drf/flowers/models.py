from django.db import models

class Flower(models.Model):
    flo_id = models.CharField(max_length=10)
    name = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
