from django.db import models

# Create your models here.

class Whell(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)
    class Meta:
        db_table = 'axf_whell'
