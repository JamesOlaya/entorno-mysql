from django.db import models

# Create your models here.

class Aprendiz(models.Model):
    name = models.CharField(max_length=10, )
    last_name = models.CharField(max_length=10)
    year_birth = models.PositiveIntegerField()
    document_num = models.CharField(max_length=15)
    document_type = models.CharField(max_length=3)
    ficha_num = models.CharField(max_length=8)