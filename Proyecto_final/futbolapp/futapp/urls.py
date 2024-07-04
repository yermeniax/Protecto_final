from django.urls import path, include
from .views import HomePageView, CustomLoginView, RegisterView, dashboard, equipos, profesores, jugadores, agregar_jugador, modificar_jugador, JugadorDeleteView, pagos
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/equipos/', equipos, name='equipos'),
    path('dashboard/profesores/', profesores, name='profesores'),
    path('dashboard/jugadores/', jugadores, name='jugadores'),
    path('dashboard/pagos/', pagos, name='pagos'),
    path('dashboard/jugadores/agregar/', agregar_jugador, name='agregar_jugador'),
    path('dashboard/jugadores/modificar/<int:pk>/', modificar_jugador, name='modificar_jugador'),
    path('dashboard/jugadores/eliminar/<int:pk>/', JugadorDeleteView.as_view(), name='eliminar_jugador'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    
]

