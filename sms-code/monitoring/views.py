from django.shortcuts import render

# Create your views here.

def lobby(request):
    return render(request, 'events/lobby.html')


def index(request):
    return render(request, 'monitoring/index.html')