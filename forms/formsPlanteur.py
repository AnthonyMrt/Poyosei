from django import forms
from django.contrib.admin import widgets
from django.forms import ModelChoiceField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from poyosei.models import *

class PlanteurForm(forms.ModelForm):
      class Meta:
        model = Planteur
        fields = '__all__'
        error_messages = {
          'nom': {
            'max_length': "Le nom écrit est trop long",
          },
        }
      def __init__(self, *args, **kwargs):
        super(PlanteurForm, self).__init__(*args, **kwargs)
        self.fields['dateNaissance'].widget = widgets.AdminDateWidget()
        self.fields['date_adhesion'].widget = widgets.AdminDateWidget()
        self.fields['date_fin_Diecte'].widget = widgets.AdminDateWidget()
        self.fields['date_cessation_Activite'].widget = widgets.AdminDateWidget()





class PacageForm(forms.Form):
      planteurSearch = forms.CharField(label='planteurSearch', max_length=100, widget=forms.TextInput(attrs={'onkeyup': 'planteur_suggestion()', 'placeholder': 'planteur_datalist',}))

      def clean_planteurSearch(self):
            try:
                  planteurSearch = int(self.cleaned_data["planteurSearch"])
            except:
                  planteurSearch = "inconnue"

            if planteurSearch and Planteur.objects.filter(pacage__contains=planteurSearch).count():
                  return planteurSearch

            else:
                raise forms.ValidationError("Veuillez entrez un pacage valide")
