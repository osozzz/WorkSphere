# archivo: core/views.py o el archivo donde esté definida la vista
from django.shortcuts import render
from event.models import Event  # Asegúrate de que 'event' es el nombre correcto de la app

def core(request):
    events = Event.objects.all()  # Obtiene todos los eventos
    return render(request, 'core/core.html', {'events': events})
