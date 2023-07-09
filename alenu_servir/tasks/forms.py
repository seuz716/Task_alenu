from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    titulo = forms.CharField(label='Título', max_length=200)
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea)
    completada = forms.BooleanField(label='Completada', required=False)
    url_imagen = forms.URLField(label='URL de la Imagen', required=False)

    class Meta:
        model = Task
        fields = ('titulo', 'descripcion', 'completada', 'url_imagen')
