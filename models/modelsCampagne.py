from django.db import models
from decimal import Decimal
from django.utils import timezone
from django.forms import DateTimeField
from datetime import datetime
from project import settings
from poyosei.models import *


class Campagne(models.Model):
    pacage = models.CharField(max_length=9)
    annee = models.CharField(max_length=4)
    rit = models.DecimalField(
        max_digits=20, decimal_places=0, default=Decimal('0.0'))
    rid = models.DecimalField(
        max_digits=20, decimal_places=0, default=Decimal('0.0'))
    production_commerciale_totale = models.DecimalField(
        max_digits=9, decimal_places=0, default=Decimal('0.0'))
    commentaire = models.TextField(blank=True)
    ri_Total = models.DecimalField(
        max_digits=20, decimal_places=0, default=Decimal('0.0'))

    class Meta:
        app_label = 'poyosei'
        unique_together = ('pacage', 'annee',)

    def __str__(self):
        return self.pacage

    def campagneExport(self, annee):
        Model = Campagne

        line = Model.objects.get(pacage=self.pacage, annee=annee)
        headers = []
        for field in Model._meta.get_fields():
            headers.append(field.name)
        row = []
        for field in headers:
            if field in headers:
                if not Model._meta.get_field(field).is_relation:
                    val = getattr(line, field)
                    # if callable(val):
                    # val = val()
                    row.append(str(val))

        return row

    @property
    def TerminerCampagne(self):
        """Fonction qui sert à cloturer la campagne en Cours"""
        reserve = Planteur.objects.get(pacage='000000000')
        annee = reserve.annee
        newAnnee = annee + 1

        planteurs = Planteur.objects.all()
        for p in planteurs:
            if p.pacage != '000000000':
                ridP = p.ridAnneeEnCours
                ritP = p.ritAnneeEnCours
                Campagne.objects.create(
                    pacage=p.pacage, annee=newAnnee, rid=ridP, rit=ritP)
            else:
                taxe = p.taxeReserve
                total = float(p.ridAnneeEnCours) + taxe
                riTemp = p.ritAnneeEnCours
                Campagne.objects.create(
                    pacage=p.pacage, annee=newAnnee, rid=total, rit=riTemp)

    def CampagneEnCours(pacageSearch='00000000'):
        """Fonction qui récupère l'année de la campagne en Cours"""
        query = Campagne.objects.filter(pacage=pacageSearch)
        p = Campagne.objects.order_by('annee').last()
        annee = p.annee
        return int(annee)
