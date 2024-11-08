# archivo: event/urls.py
from django.urls import path
from .views import create_event, event_detail

urlpatterns = [
    path('create/', create_event, name='create_event'),
    path('<int:event_id>/', event_detail, name='event_detail'),
]
