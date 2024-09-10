from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pour l'interface d'administration
    path('', include('main_app.urls')),  # Inclut les URLs de l'application principale
]

# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('registres/', views.registres, name='registres'),  # Page des vidéos
    path('poemes/', views.poemes, name='poemes'),  # Page des poèmes
    path('memoire/', views.memoire, name='memoire'),  # Page du mémoire
    path('a-propos/', views.a_propos, name='a_propos'),  # Page "À propos"
]