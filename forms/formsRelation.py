from django import forms
from django.contrib.admin import widgets
from django.forms import ModelChoiceField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from poyosei.models import *


class RelationForm(forms.ModelForm):
  class Meta:
    model = Relation
    fields = '__all__'

  def clean(self):
    pacageA = self.cleaned_data['pacageA']
    filterA = Planteur.objects.filter(pacage=pacageA)

    if not filterA:
      raise forms.ValidationError('Veuillez entrer un pacages valide')

