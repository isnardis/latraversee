from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def registres(request):
    return HttpResponse("Vidéos")

def poemes(request):
    return HttpResponse("Poèmes")

def memoire(request):
    return HttpResponse("Le mémoire")

def a_propos(request):
    return HttpResponse("`À propos")
