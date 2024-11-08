# archivo: event/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm, CommentForm
from .models import Event

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()  # Guarda el evento y lo asigna a la variable 'event'
            return redirect('event_detail', event_id=event.id)  # Redirige al detalle usando el ID del evento
    else:
        form = EventForm()
    return render(request, 'event/create_event.html', {'form': form})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    comments = event.comments.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.event = event
            new_comment.author = request.user
            new_comment.save()
            event.update_rating()  # Actualizar el rating del evento
            return redirect('event_detail', event_id=event.id)
    else:
        comment_form = CommentForm()
    return render(request, 'event/event_detail.html', {
        'event': event,
        'comments': comments,
        'comment_form': comment_form,
    })
