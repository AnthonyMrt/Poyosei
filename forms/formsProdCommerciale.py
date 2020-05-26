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

class ProdCommercialeForm(forms.ModelForm):
    class Meta:
        model = ProductionCommerciale
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProdCommercialeForm, self).__init__(*args, **kwargs)
        self.fields['pacage'] = forms.ModelChoiceField(queryset=Planteur.objects.all())
        self.fields['année'] = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=datetime.now().year)

