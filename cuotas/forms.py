from django import forms
from .models import Cuota

class CuotaForm(forms.ModelForm):
    class Meta:
        model = Cuota
        fields = ["monto", "periodo", "fecha_limite"]
