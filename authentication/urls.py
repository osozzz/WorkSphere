# archivo: myapp/urls.py
from django.urls import path
from .views import register, CustomLoginView, edit_profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit-profile/', edit_profile, name='edit_profile'),

]
