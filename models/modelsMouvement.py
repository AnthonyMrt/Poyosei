from django.db import models
from decimal import Decimal
from django.utils import timezone
from django.forms import DateTimeField
from project import settings
from datetime import datetime
from poyosei.models import *
from django.core.validators import MaxValueValidator, MinValueValidator
from simple_history.models import HistoricalRecords


typeMouvement_CHOICE = (
    ('transfert total d\'une exploitation', 'transfert total d\'une exploitation'),
    ('Transfert de référence rndividuelle avec cession partielle de foncier',
     'Transfert de référence individuelle avec cession partielle de foncier'),
    ('Transfert de référence individuelle sans foncier',
     'Transfert de référence individuelle sans foncier'),
    ('Reprise administrative', 'Reprise administrative'),
    ('Cession volontaire définitive', 'Cession volontaire définitive'),
    ('Cession volontaire temporaire', 'Cession volontaire temporaire'),
    ('Cessation d’activite sans repreneur', 'Cessation d’activite sans repreneur'),
    ('Attribution de Reference Individuelle par la reserve',
     'Attribution de Reference Individuelle par la réserve'),
    ('Autre', 'Autre'),
    ('', ''),
)


class typeMouvementModel(models.Model):
    type_mouvement = models.CharField(
        max_length=100, choices=typeMouvement_CHOICE, default='')
    informations = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)


typeDeReferenceIndividuelle_CHOICE = (
    ('définitive', 'définitive'),
    ('temporaire', 'temporaire'),
    ('autre', 'autre'),
    ('', '')
)


class Mouvement(typeMouvementModel):
    pacage_cedant = models.CharField(max_length=10)
    pacage_repreneur = models.CharField(max_length=10)
    année_concerne = models.CharField(max_length=4, blank=True)
    date_demande = models.DateField(null=True, blank=True)
    mouvement_valide = models.BooleanField(default=False, blank=True)
    date_COSDA_Valide = models.DateField(null=True, blank=True)
    type_reference_individuelle_modifie = models.CharField(
        max_length=100, default='', choices=typeDeReferenceIndividuelle_CHOICE)
    quantite_reference_individuelle_demande = models.DecimalField(
        max_digits=10, decimal_places=0, default=Decimal('0'), blank=True, null=True)
    quantite_reference_individuelle_accorde = models.DecimalField(
        max_digits=10, decimal_places=0, default=Decimal('0'), blank=True)
    date_creation = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    taxe = models.FloatField(default=0.0, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.id)

    def mouvementExport(self):
        Model = Mouvement

        line = Model.objects.get(
            pacage_cedant=self.pacage_cedant, pacage_repreneur=self.pacage_repreneur)
        headers = []
        for field in Model._meta.get_fields():
            headers.append(field.name)
        row = []
        for field in headers:
            if field in headers:
                if not Model._meta.get_field(field).is_relation:
                    val = getattr(line, field)
                    row.append(str(val))

        return row

    # Transfert de Référence Individuelle sans foncier
    @property
    def ridCedant(self):
        """Fonction qui effectue le calcul la nouvelle référence individuelle du pacage cédant lors d'un mouvement."""
        ceder = - self.quantite_reference_individuelle_accorde
        if self.type_mouvement == 'Reprise administrative':
            c = Campagne.objects.order_by('annee').last()
            Cannee = int(c.annee)
            cR = Campagne.objects.get(pacage=self.pacage_cedant, annee=Cannee)
            produc_commer = float(cR.production_commerciale_totale)
            print(produc_commer)
            print(self.quantite_reference_individuelle_accorde)
            ceder = - \
                float(self.quantite_reference_individuelle_accorde) * \
                0.80 + produc_commer

        return ceder

    @property
    def ridRepreneur(self):
        """Fonction qui effectue le calcul de la nouvelle référence"""
        taxer = float(
            self.quantite_reference_individuelle_accorde) * self.taxe/100
        repris = float(self.quantite_reference_individuelle_accorde) - taxer
        if self.type_mouvement == 'Reprise administrative':
            c = Campagne.objects.order_by('annee').last()
            Cannee = int(c.annee)
            cR = Campagne.objects.get(pacage=self.pacage_cedant, annee=Cannee)
            produc_commer = float(cR.production_commerciale_totale)
            # print(produc_commer)
            repris = float(
                self.quantite_reference_individuelle_accorde) * 0.80 - produc_commer

        return repris

    @property
    def ridReserve(self):
        retenue = float(
            self.quantite_reference_individuelle_accorde) * self.taxe/100
        return retenue

    @property
    def ritCedant(self):
        donner = 0
        return donner

    @property
    def ritRepreneur(self):
        obtenue = 0
        return obtenue

    @property
    def ritReserve(self):
        taxe = 0
        return taxe

    # Transfert de Référence individuelle avec cession partielle de foncier:
    # def cederFoncier(self):
        # query = Campagne.objects.order_by('annee').last()
        # annee1 = query.annee - 1
        # annee2 = query.annee
        # mvt1 = Mouvement.objects.filter(type_mouvement='Attribution de Reference Individuelle par la reserve', pacage_repreneur=self.pacage_repreneur, année_concerne=annee1)
        # mvt2 = Mouvement.objects.filter(type_mouvement='Attribution de Reference Individuelle par la reserve', pacage_repreneur=self.pacage_repreneur, année_concerne=annee2)
        # mvt3 = Mouvement.objects.filter(type_mouvement='Attribution de Reference Individuelle par la reserve', pacage_repeneur=self.pacage_repreneur, année_cocerne=datetime.now().year)
        # mvt4 = Mouvement.objects.filter(pacage_repeneur=self.pacage_repreneur, année_cocerne=datetime.now().year)
        # cpg = Campagne.objects.get(pacage=self.pacage_repreneur, annee=query.annee)
        # quantite1 = mvt1.count()
        # quantite2 = mvt2.count()
        # quantite3 = mvt3.count()
        # quantite4 = mvt4.count()
        # total = quantite1 + quantite2 + quantite3

        # if total > 1 or quantite4 > 2 :
        # return False
        # else:
        # ceder = - self.quantite_reference_individuelle_accorde
        # return ceder

    # def obtenueFoncier(self):
        # query = Campagne.objects.order_by('annee').last()
        # annee1 = query.annee - 1
        # annee2 = query.annee
        # mvt1 = Mouvement.objects.filter(pacage_repreneur=self.pacage_repreneur, année_concerne=annee1)
        # mvt2 = Mouvement.objects.filter(pacage_repreneur=self.pacage_repreneur, année_concerne=annee2)
        # mvt3 = Mouvement.objects.filter(pacage_repeneur=self.pacage_repreneur, année_cocerne=datetime.now().year)
        # quantite1 = mvt1.count()
        # quantite2 = mvt2.count()
        # quantite3 = mvt3.count()
        # total = quantite1 + quantite2 + quantite3

        # if total > 1:
        # return False
        # else:
        # obtenue = self.quantite_reference_individuelle_accorde
        # return obtenue
