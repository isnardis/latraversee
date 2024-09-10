from django.db import models

class Video(models.Model):
    # Choix pour le champ 'language'
    LANGUAGE_CHOICES = [
        ('PT', 'Portugais'),
        ('FR', 'Français'),
        ('BI', 'Bilingue'),
    ]
    # Choix pour le champ 'location'
    LOCATION_CHOICES = [
        ('EX', "À l'extèrieur"),
        ('IN', "À l'intèrieur"),
    ]
    # Choix pour le champ 'has_music'
    MUSIC_CHOICES = [
        ('M', 'Avec musique'),
        ('N', 'Sans musique'),
    ]

    title = models.CharField(max_length=200)  # Titre de la vidéo
    video_file = models.FileField(upload_to='videos/')  # Fichier vidéo
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)  # Langue de la vidéo
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES)  # Lieu de tournage (EX ou IN)
    has_music = models.CharField(max_length=1, choices=MUSIC_CHOICES)  # Présence de musique (M ou N)

class Poem(models.Model):
    # Choix pour le champ 'language'
    LANGUAGE_CHOICES = [
        ('PT', 'Portugais'),
        ('FR', 'Français'),
        ('BI', 'Bilíngue'),
    ]

    title = models.CharField(max_length=200)  # Titre du poème
    content = models.TextField()  # Contenu du poème
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)  # Langue du poème

class Memoire(models.Model):
    title = models.CharField(max_length=200)  # Titre du mémoire
    content = models.TextField()  # Contenu du mémoire
    file = models.FileField(upload_to='memoires/')  # Fichier du mémoire
