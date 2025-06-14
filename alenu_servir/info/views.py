from django.shortcuts import render
from tasks.models import Task

def programas_view(request):
    tasks = Task.objects.all()
    return render(request, 'info/programas.html', {
        'tasks': tasks,
    })

def mision_view(request):
    return render(request, 'info/mision.html')


def participa_view(request):
    return render(request, 'info/participa.html')

def contacto_view(request):
    return render(request, 'info/contacto.html')    

def transparencia_view(request):
    return render(request, 'info/transparencia.html')



