from django import forms
from django.contrib.admin import widgets
from django.forms import ModelChoiceField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from poyosei.models import *
from datetime import datetime

def year_choices():
    return [(r,r) for r in range(datetime.now().year-4, datetime.now().year+5)]

class MouvementForm(forms.ModelForm):
      class Meta:
            model = Mouvement
            fields = '__all__'

      def __init__(self, *args, **kwargs):
        super(MouvementForm, self).__init__(*args, **kwargs)
        self.fields['type_mouvement'].widget.attrs\
            .update({
                'placeholder': 'Name',
                'class': 'form-group'
            })
        self.fields['mouvement_valide'].widget.attrs\
            .update({
                'type': 'checkbox',
                'class': 'custom-control-input'
              })
        self.fields['type_mouvement'] = forms.ModelChoiceField(queryset=typeMouvement.objects.all(), widget=forms.Select(attrs={"onChange": 'javascript: dynamicdropdown(this.options[this.selectedIndex].value);'}))
        self.fields['date_demande'].widget = widgets.AdminDateWidget()
        #self.fields['informations'].widget = forms.Select(attrs={"onChange": 'javascript: dynamicdropdown(this.options[this.selectedIndex].value);'})
        self.fields['date_COSDA_Valide'].widget = widgets.AdminDateWidget()
        self.fields['pacage_cedant'] = forms.ModelChoiceField(queryset=Planteur.objects.all())
        self.fields['pacage_repreneur'] = forms.ModelChoiceField(queryset=Planteur.objects.all())
        self.fields['année_concerne'] = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=datetime.now().year)

