from django import forms
from django.contrib.admin import widgets
from django.forms import ModelChoiceField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from poyosei.models import *

class TonnageForm(forms.ModelForm):
    class Meta:
        model = reconstitutionTonnage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TonnageForm, self).__init__(*args, **kwargs)
        self.fields['pacage'] = forms.ModelChoiceField(queryset=Planteur.objects.all())