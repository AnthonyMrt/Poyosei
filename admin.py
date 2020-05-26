from django.contrib import admin
from django.forms import TextInput, Textarea
#from simple_history.admin import SimpleHistoryAdmin
from .models import *


# Register your models here.


class PlanteurHistoryAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'pacage', 'controle')
    history_list_display = ['controle']
    date_hierarchy = 'date_creation'
    search_fields = ['name', 'user__username']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }


class reconstitutionTonnageAdmin(admin.ModelAdmin):
    model = reconstitutionTonnage
    list_display = ('pacage', 'annee', 'reconstitution_tonnage', 'justification')

class CampagneAdmin(admin.ModelAdmin):
    model = Campagne
    list_display = ('pacage', 'annee', 'rid', 'rit')
    extra = 1

class StatistiqueAdmin(admin.ModelAdmin):
    model = Statistique
    list_display = ('pacage', 'annee', 'surface_totale_utile', 'surface_totale_exploitation')

class MouvementAdmin(admin.ModelAdmin):
    model = Mouvement
    list_display = ('type_mouvement', 'pacage_cedant', 'pacage_repreneur', 'date_demande', 'mouvement_valide' )

class typeMouvementModelsAdmin(admin.ModelAdmin):
    model = typeMouvementModel
    list_display = ('type_mouvement', 'informations')


class RelationAdmin(admin.ModelAdmin):
    model = Relation
    list_display = ('id', 'pacageA')

class prodCommercialeAdmin(admin.ModelAdmin):
    model = ProductionCommerciale
    list_display = ('pacage', 'année', 'production_commerciale')

class typeMouvementAdmin(admin.ModelAdmin):
    model = typeMouvement



admin.site.register(Planteur, PlanteurHistoryAdmin)
admin.site.register(Mouvement, MouvementAdmin)
admin.site.register(typeMouvementModel, typeMouvementModelsAdmin)
admin.site.register(Campagne, CampagneAdmin)
admin.site.register(reconstitutionTonnage, reconstitutionTonnageAdmin)
admin.site.register(Statistique, StatistiqueAdmin)
admin.site.register(Relation, RelationAdmin)
admin.site.register(ProductionCommerciale, prodCommercialeAdmin)
admin.site.register(typeMouvement, typeMouvementAdmin)


