from django import forms
from .models import Cobro

class CobroForm(forms.ModelForm):
    class Meta:
        model = Cobro
        fields = ["habitante", "periodo", "monto", "estado"]
