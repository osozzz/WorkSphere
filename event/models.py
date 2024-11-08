from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    
    # Relaciones y categorías
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    
    # Imágenes del evento
    ticket_image = models.ImageField(upload_to='event/tickets/')
    poster_image = models.ImageField(upload_to='event/posters/')
    flyer_image = models.ImageField(upload_to='event/flyers/')
    
    # Atributos adicionales
    attendees_count = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)  # Media de rating de comentarios

    def __str__(self):
        return self.title

    def update_attendees_count(self):
        """Método para actualizar el número de asistentes basado en los usuarios registrados."""
        self.attendees_count = self.attendees.count()  # Esto supone una relación M2M con asistentes
        self.save()

    def update_rating(self):
        """Método para actualizar el rating promedio basado en los comentarios."""
        comments = self.comments.all()
        if comments.exists():
            self.rating = sum([comment.rating for comment in comments]) / comments.count()
        else:
            self.rating = 0
        self.save()
        
class Comment(models.Model):
    RATING_CHOICES = [(i, f"{i} estrellas") for i in range(1, 6)]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.author} en {self.event}"