from django.db import models

class Cricketer(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=30)
    nation = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
