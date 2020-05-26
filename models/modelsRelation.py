from django.db import models
# from decimal import Decimal
# from project import settings
from .modelsPlanteur import *
# import datetime


class Relation(models.Model):
    pacageA = models.CharField(max_length=9, default="")
    planteurs = models.ManyToManyField(Planteur)

    def __str__(self):
        return "%s" % (self.pacageA)
