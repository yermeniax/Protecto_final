from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegistrationForm  # Asegúrate de tener este formulario definido
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Equipo, Profesor, Jugador, Pago
from django.contrib.auth import logout  # Importa la función de logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Jugador
from .forms import JugadorForm
from django.views.generic import CreateView, UpdateView, DeleteView

class HomePageView(TemplateView):
    template_name = 'futapp/home.html'

class CustomLoginView(LoginView):
    template_name = 'futapp/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'futapp/register.html'
    success_url = reverse_lazy('login')

@login_required
def dashboard(request):
    return render(request, 'futapp/dashboard.html')

def handle_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Procesa el formulario, por ejemplo, guarda el usuario en la base de datos
            return HttpResponseRedirect(reverse('success'))  # Redirige a una página de éxito
    else:
        form = RegistrationForm()

    return render(request, 'futapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirigir a la página de inicio después de iniciar sesión
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'futapp/dashboard.html')

@login_required
def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'futapp/equipos.html', {'equipos': equipos})

@login_required
def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'futapp/profesores.html', {'profesores': profesores})

@login_required
def jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'futapp/jugadores.html', {'jugadores': jugadores})

@login_required
def jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'futapp/jugadores.html', {'jugadores': jugadores})

@login_required
def agregar_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jugadores')
    else:
        form = JugadorForm()
    return render(request, 'futapp/agregar_jugador.html', {'form': form})

@login_required
def modificar_jugador(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    if request.method == 'POST':
        form = JugadorForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect('jugadores')
    else:
        form = JugadorForm(instance=jugador)
    return render(request, 'futapp/modificar_jugador.html', {'form': form})

class JugadorDeleteView(DeleteView):
    model = Jugador
    template_name = 'futapp/eliminar_jugador.html'
    success_url = reverse_lazy('jugadores')

@login_required
def pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'futapp/pagos.html', {'pagos': pagos})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirige al usuario a la página de inicio
