from django.db import models
from decimal import Decimal
from django.utils import timezone
from django.forms import DateTimeField
from project import settings
from django.db.models import Q
from django.db.models.signals import post_save
from poyosei.models import *
from django.shortcuts import get_object_or_404
from datetime import datetime
from simple_history.models import HistoricalRecords
from django.db.models import ForeignKey
from statistics import *


CIVILITE_CHOICE = (
    ('Mr', 'Monsieur'),
    ('gérant', 'Mr le gérant'),
    ('gérante', 'Mme la gérante'),
    ('Mme', 'Madame'),
    ('Societe', 'Societe'),
    ('Autre', 'Autre'),
    ('', '')
)


class Planteur(models.Model):
    pacage = models.CharField("Numéro pacage", max_length=9,
                              primary_key=True, help_text="Un nombre de 9 chiffres")
    civilite = models.CharField(
        "Civilité", max_length=20, choices=CIVILITE_CHOICE, default='', blank=True)
    nom = models.CharField("Nom", max_length=200,
                           help_text="200 caractères maximum.")
    prenom = models.CharField("Prénom", max_length=100,
                              help_text="200 caractères maximum.")
    siret = models.CharField("SIRET", max_length=14, blank=True,
                             help_text="code Insee permettant l'identification d'un établissement ou d'une entreprise française.", null=True)
    LPG = models.CharField("Numéro LPG", max_length=100, blank=True,
                           help_text="Identifiant LPG du planteur.", null=True)
    contre_marque = models.CharField(
        "Contremarque", max_length=100, blank=True, null=True)
    denomination = models.TextField(
        "Dénomination", help_text="Texte d'aide", null=True, max_length=100, blank=True)
    gerant = models.TextField(
        "Gérant", help_text="Texte d'aide", null=True, blank=True)
    adresse = models.CharField(
        "Adresse", help_text="Adresse du planteur", max_length=255, null=True, blank=True)
    adresse_complementaire = models.CharField(
        max_length=255, null=True, blank=True)
    code_postal = models.CharField(
        "Code postal", help_text="Code postal planteur", null=True, max_length=10, blank=True)
    commune = models.CharField(
        "Commune", max_length=100, help_text="Commune du planteur", blank=True, null=True)
    telephone_principale = models.CharField(
        "Numéro de téléphone", null=True, help_text='Téléphone de contact', max_length=50, blank=True)
    telephone_secondaire = models.CharField(
        "Autre téléphone",  help_text='téléphone de contact', max_length=50, null=True, blank=True)
    courriel = models.EmailField(
        "Courriel", help_text="Adresse de courriel de contact.", null=True, blank=True)
    dateNaissance = models.DateField(
        "Date de naissance", help_text="Date de naissance du planteur", null=True, blank=True)
    date_adhesion = models.DateField(
        "Date d'adhésion à l'organisme de production", help_text="Date adhésion", null=True, blank=True)
    numero_exemption_Diecte = models.CharField(
        "Numéro d'exemption DIECTE", help_text="Numéro d'exemption DIECTE", max_length=50, null=True, blank=True)
    date_fin_Diecte = models.DateField(
        "Date de fin d'exemption DIECTE", help_text="Date de fin d'exemption DIECTE", null=True, blank=True)
    entreprise_associé = models.TextField(
        "Entreprise associé par Actionnaire", help_text="Autre entreprise associé", null=True, blank=True)
    controle = models.BooleanField(
        "Exemption de contrôle", help_text='Le planteur est-il exempte de contrôle ?', default=False, blank=True)
    date_cessation_Activite = models.DateField(
        "Date de cessation d'activité", help_text="Date de cessation d'activité", null=True, blank=True)
    commentaire = models.TextField(
        "Commentaire", help_text="Toute information utile à l'instruction", null=True, blank=True)
    date_creation = models.DateField(auto_now_add=True, null=True, blank=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ['pacage']

    def __str__(self):
        """Pour chaque methode ajouter sa fonction."""
        return self.pacage

    def save(self, *args, **kwargs):
        """fonction qui crée et sauvegarde un planteur tout en lui créeant des campagnes et des statistiques vide de données pour les années antérieurs."""
        listeAnnee = Campagne.objects.values_list(
            'annee', flat=True).distinct()
        for annee in listeAnnee:
            from poyosei.models import Statistique
            if Campagne.objects.filter(pacage=self.pacage, annee=annee).exists() and Statistique.objects.filter(pacage=self, annee=annee).exists():
                super(Planteur, self).save(*args, **kwargs)
            else:
                Campagne.objects.create(pacage=self.pacage, annee=annee, rid=0.0, rit=0.0, commentaire='Pas de données disponible pour cette campagne') and Statistique.objects.create(
                    pacage=self, annee=annee, commentaire='Pas de données statistiques disponibles pour cette année')

                super(Planteur, self).save(*args, **kwargs)

    def get_fk_model(model, fieldname):
        field_object = model._meta.get_field(fieldname)
        if field_object.is_relation:
            return True
        return False

    def planteurExport(self):
        """Fonction qui récupère les noms des champs de la table planteur pour les transmettre dans les rapports de type CSV"""
        Model = Planteur

        line = Model.objects.get(pacage=self.pacage)
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

    def annee():
        return int(Campagne.CampagneEnCours())

    @property
    def ridAnneeP(self):
        """Fonction qui recupère la référence individuelle définitive du planteur pour l'année précédent l'année de la campagne en cours."""
        rid = float(self.ridDerniereCampagne)
        mvtCedant = Mouvement.objects.filter(
            pacage_cedant=self.pacage, type_reference_individuelle_modifie='définitive', année_concerne=Campagne.CampagneEnCours() - 1)
        for mvt in mvtCedant:
            rid += float(mvt.ridCedant)

        mvtRepreneur = Mouvement.objects.filter(
            pacage_repreneur=self.pacage, type_reference_individuelle_modifie='définitive', année_concerne=Campagne.CampagneEnCours() - 1)
        for mvt in mvtRepreneur:
            rid += float(mvt.ridRepreneur)

        return rid

    @property
    def ritAnneeP(self):
        """Fonction qui recupère la référence individuelle temporaire du planteur pour l'année précédent l'année de la campagne en cours."""
        rit = 0
        mvtCedant = Mouvement.objects.filter(
            pacage_cedant=self.pacage, type_reference_individuelle_modifie='temporaire', année_concerne=Campagne.CampagneEnCours() - 1)
        for mvt in mvtCedant:
            rit += float(mvt.ridCedant)

        mvtRepreneur = Mouvement.objects.filter(
            pacage_repreneur=self.pacage, type_reference_individuelle_modifie='temporaire', année_concerne=Campagne.CampagneEnCours() - 1)
        for mvt in mvtRepreneur:
            rit += float(mvt.ridRepreneur)

        return rit

    @property
    def ridDerniereCampagne(self):
        """Fonction qui renvoie la rid de la dernière campagne"""
        query = Campagne.objects.filter(pacage=self.pacage)
        p = query.order_by('annee').last()
        ri = p.rid
        return ri

    @property
    def ridCampagneP(self):
        """Fonction qui renvoie la rid a campagne précédent la dernière campagne"""
        query = Campagne.objects.filter(pacage=self.pacage)
        p = query.order_by('annee').last() - 1
        ri = p.rid

        return ri

    @property
    def ritDerniereCampagne(self):
        """Fonction qui recupère la rid de la campagne précédent la campagne en cours"""
        query = Campagne.objects.filter(pacage=self.pacage)
        p = query.order_by('annee').last()
        ri = p.rit
        return ri

    @property
    def ridAnneeEnCours(self):
        """Fonction qui récupère la référence individuelle du planteur pour la campagne en cours"""
        rid = float(self.ridDerniereCampagne)
        mvtCedant = Mouvement.objects.filter(
            pacage_cedant=self.pacage, type_reference_individuelle_modifie='définitive', année_concerne=Campagne.CampagneEnCours())
        for mvt in mvtCedant:
            rid += float(mvt.ridCedant)

        mvtRepreneur = Mouvement.objects.filter(
            pacage_repreneur=self.pacage, type_reference_individuelle_modifie='définitive', année_concerne=Campagne.CampagneEnCours())
        for mvt in mvtRepreneur:
            rid += float(mvt.ridRepreneur)

        return rid

    @property
    def ritAnneeEnCours(self):
        """Fonction qui recupère la référence individuelle temporaire du planteur pour la campagne en cours"""
        rit = 0
        mvtCedant = Mouvement.objects.filter(
            pacage_cedant=self.pacage, type_reference_individuelle_modifie='temporaire', année_concerne=Campagne.CampagneEnCours())
        for mvt in mvtCedant:
            rit += float(mvt.ridCedant)

        mvtRepreneur = Mouvement.objects.filter(
            pacage_repreneur=self.pacage, type_reference_individuelle_modifie='temporaire', année_concerne=Campagne.CampagneEnCours())
        for mvt in mvtRepreneur:
            rit += float(mvt.ridRepreneur)

        return rit

    @property
    def riTotale(self):
        """Fonction qui calcule la référence individuelle totale pour l'année en cours"""
        if self.pacage == '000000000':
            total = self.ridAnneeEnCours + self.ritAnneeEnCours + self.taxeReserve
        else:
            total = self.ridAnneeEnCours + self.ritAnneeEnCours

        return total

    @property
    def ridAnneeEnCoursMvtenAttente(self):
        """Fonction qui renvoie la rid en cours en comptabilisant les mouvements non valide"""
        rid = float(self.ridDerniereCampagne)
        ridFalse = float(0)
        mvtCedantTrue = Mouvement.objects.filter(
            pacage_cedant=self.pacage, type_reference_individuelle_modifie='définitive', mouvement_valide=True)
        mvtCedantFalse = Mouvement.objects.filter(
            pacage_cedant=self.pacage, type_reference_individuelle_modifie='définitive', mouvement_valide=False)
        for mvt in mvtCedantTrue:
            rid += float(mvt.ridCedant)
        for mvt in mvtCedantFalse:
            ridFalse += float(mvt.ridCedant)
        mvtRepreneur = Mouvement.objects.filter(
            pacage_repreneur=self.pacage, type_reference_individuelle_modifie='définitive', mouvement_valide=True)
        mvtRepreneurFalse = Mouvement.objects.filter(
            pacage_repreneur=self.pacage, type_reference_individuelle_modifie='définitive', mouvement_valide=False)
        for mvt in mvtRepreneur:
            rid += float(mvt.ridRepreneur)
        for mvt in mvtRepreneurFalse:
            ridFalse += float(mvt.ridRepreneur)

        return ridFalse

    @property
    def ritAnneeEnCoursMvtTemporaire(self):
        """Fonction qui renvoie la rit"""
        rit = float(self.ritDerniereCampagne)
        ritFalse = float(0)
        mvtCedantTrue = Mouvement.objects.filter(
            pacage_cedant=self.pacage, type_reference_individuelle_modifie='temporaire', mouvement_valide=True)
        mvtCedantFalse = Mouvement.objects.filter(
            pacage_cedant=self.pacage, type_reference_individuelle_modifie='temporaire', mouvement_valide=False)
        for mvt in mvtCedantTrue:
            rit += float(mvt.ritCedant)
        for mvt in mvtCedantFalse:
            ritFalse += float(mvt.ritCedant)
        mvtRepreneur = Mouvement.objects.filter(
            pacage_repreneur=self.pacage, type_reference_individuelle_modifie='temporaire', mouvement_valide=True)
        mvtRepreneurFalse = Mouvement.objects.filter(
            pacage_repreneur=self.pacage, type_reference_individuelle_modifie='temporaire', mouvement_valide=False)
        for mvt in mvtRepreneur:
            rit += float(mvt.ritRepreneur)
        for mvt in mvtRepreneurFalse:
            ritFalse += float(mvt.ritRepreneur)

        return ritFalse

    @property
    def taxeReserve(self):
        """Fonction qui récupère la taxe percu sur la réserve sur les mouvements de la campagne en cours."""
        reserve = Planteur.objects.get(pacage='000000000')
        ri = 0
        p = Campagne.objects.order_by('annee').last()
        annee = p.annee
        mvt = Mouvement.objects.all()
        for m in mvt:
            if m.type_mouvement == 'Transfert de Référence Individuelle sans foncier' and m.année_concerne == annee:
                ri += float(m.ridReserve)

        return ri

    @property
    def ridAnneePrecedente(self, annee):
        cPre = Campagne.objects.get(pacage=self.pacage, annee=annee)
        ridPre = cPre.rid

        return ridPre

    @property
    def totalRI(self):
        planteurs = Planteur.objects.all()
        reserve = Planteur.objects.get(pacage='000000000')
        ri = float(reserve.ridDerniereCampagne)
        C = Campagne.objects.order_by('annee').last()
        annee = C.annee
        mvt = Mouvement.objects.all()
        for m in mvt:
            if m.type_mouvement == 'Transfert de Référence Individuelle sans foncier' and m.année_concerne == annee:
                ri += float(m.ridReserve)

        for p in planteurs:
            if p.pacage != reserve.pacage:
                total = float(p.ridAnneeEnCours)+float(p.ritAnneeEnCours)
            elif p.pacage == reserve.pacage:
                total = float(ri)+float(p.ritAnneeEnCours)

        return total

    @property
    def prodCommercialeTotale(self, annee):
        """Fonction qui calcule la production commerciale totale"""
        tonnageReconstitué = reconstitutionTonnage.objects.get(
            pacage=self.pacage, annee=annee)
        stats = Statistique.objects.get(pacage=self.pacage, annee=annee)
        total = tonnageReconstitué.reconstitution_tonnage + \
            stats.production_exporte + stats.production_locale

        return total

    @property
    def moyenneOlympique(self):
        """Fonction qui calcule la moyenne olympique"""
        year = Campagne.objects.values_list('annee', flat=True).last()
        i = int(year)
        y = i
        rang = []
        while i > y - 5:
            rang.append(i)
            i -= 1
        tabRI = []
        for y in year:
            p = Campagne.objects.get(pacage=self.pacage, annee=y)
            ri = p.riTotale
            tabRI.append(ri)
            maxi = max(tabRI)
            mini = min(tabRI)
            tabRI.remove(Maxi)
            tabRI.remove(Mini)
            moy = mean(tabRI)

        return moy
