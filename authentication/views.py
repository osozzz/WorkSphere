from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect('edit_profile')
        else:
            messages.error(request, "Por favor corrige los errores a continuación.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True  # Redirige a usuarios ya autenticados a la URL de redirección
    next_page = 'core'  # Asegura la redirección a 'core'

    def form_invalid(self, form):
        messages.error(self.request, "Nombre de usuario o contraseña incorrectos.")
        return super().form_invalid(form)
    
@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado exitosamente.")
            return redirect('core')  # Redirige a la página principal después de guardar el perfil
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'auth/edit_profile.html', {'form': form})