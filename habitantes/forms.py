from django import forms
from .models import Habitante

class HabitanteForm(forms.ModelForm):
    class Meta:
        model = Habitante
        fields = ["nombre", "domicilio", "telefono"]