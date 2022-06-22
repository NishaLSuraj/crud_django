from django.db import models

# Create your models here.
class todotable(models.Model):
    title=models.CharField(max_length=256)
 