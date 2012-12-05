# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *

def hello(request):
  return HttpResponse("Hello World")

def getPlayers(request):
  player_list = ShanghiPlayers.objects.all()
  return render_to_response('index.html', {'player_list': player_list})
