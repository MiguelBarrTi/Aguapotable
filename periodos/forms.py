from django import forms
from .models import Periodo

class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ["nombre", "fecha_inicio", "fecha_fin"]
