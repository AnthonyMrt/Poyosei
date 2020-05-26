from import_export import resources, fields
from .models import *
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget


class PlanteurResource(resources.ModelResource):
    #nom_planteur = fields.Field(attribute='planteur_nom')
    #rid = fields.Field(column_name='Référence individuelle définitive', attribute='campagne', widget=ForeignKeyWidget('poyosei:Campagne', field='rid'))
    class Meta:
        model = Planteur
        #fields = ('planteur_nom')



class mouvementResource(resources.ModelResource):
    class Meta:
        model = Mouvement


