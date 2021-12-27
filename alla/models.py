from django.db import models

# Create your models here.
class EpData(models.Model):
    name = models.CharField(max_length=70)
    date = models.CharField(max_length=30)
    epnum = models.IntegerField()
    details = models.TextField()
    
    def __str__(self):
        return str(self.epnum)