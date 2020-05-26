from django.db import models
from decimal import Decimal
# from django.utils import timezone
# from django.forms import DateTimeField
# from datetime import datetime
# from project import settings
from poyosei.models import *


class ProductionCommerciale(models.Model):
    pacage = models.CharField(max_length=9)
    année = models.CharField(max_length=4)
    production_commerciale = models.DecimalField(
        max_digits=9, decimal_places=0, default=Decimal('0'))

    class Meta:
        app_label = 'poyosei'
        unique_together = ('pacage', 'année',)

    def __str_(self):
        return self.pacage
