from django import forms
from .models import Donacion

class DonacionForm(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = ['entidad', 'tipo_regimen', 'identificacion', 'tipo_identificacion', 'ciudad', 'monto', 'proposito', 'fuente', 'url_imagen', 'descripcion']

    def clean_identificacion(self):
        identificacion = self.cleaned_data['identificacion']
        if identificacion < 1000 or identificacion > 999999999999999:
            raise forms.ValidationError("La identificación debe ser un número entre 1000 y 999999999999999.")
        return identificacion

    def clean_url_imagen(self):
        url_imagen = self.cleaned_data['url_imagen']
        if not url_imagen:
            raise forms.ValidationError("La URL de la imagen es obligatoria.")
        return url_imagen
