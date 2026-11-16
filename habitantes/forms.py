from django import forms
from .models import Habitante

class HabitanteForm(forms.ModelForm):

    class Meta:

        model = Habitante

        fields = [
            'curp',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'telefono',
            'domicilio',
            'numero_exterior',
            'numero_interior',
            'codigo_postal',
            'lineas_domicilio'
        ]
        
        widgets = {

            'curp': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'nombre': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'apellido_paterno': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'apellido_materno': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'telefono': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'domicilio': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'numero_exterior': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'numero_interior': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'codigo_postal': forms.TextInput(
                attrs={'class':'form-control'}
            ),

            'lineas_domicilio': forms.NumberInput(
                attrs={'class':'form-control'}
            )

        }