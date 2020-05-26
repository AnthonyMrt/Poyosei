from django.db import models 
# from decimal import Decimal
# from django.utils import timezone
# from django.forms import DateTimeField
# from project import settings
# from django.db.models import Q
# from django.db.models.signals import post_save
from poyosei.models import *
# from django.shortcuts import get_object_or_404
# from datetime import datetime
# from itertools import chain
# from simple_history.models import HistoricalRecords



class typeMouvement(models.Model):
    Nom_mouvement               = models.TextField(max_length=100)
    informations                = models.TextField(blank=True)

    def __str__(self):
        return str(self.Nom_mouvement)