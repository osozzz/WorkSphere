# archivo: event/forms.py
from django import forms
from .models import Event, Comment

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 'description', 'date', 'organizer', 'category', 
            'location', 'ticket_image', 'poster_image', 'flyer_image'
        ]
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Selector de fecha y hora
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['rating', 'message']
        widgets = {
            'rating': forms.RadioSelect(),  # Para mostrar el rating como estrellas
        }