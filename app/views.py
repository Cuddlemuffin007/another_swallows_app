from django.shortcuts import render, render_to_response
from app.models import Stat

def index(request):
    all_players = Stat.objects.all()
    return render_to_response('index.html', {'players': all_players})
