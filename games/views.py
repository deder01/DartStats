# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login
from models import *
from forms import *

def Home(request):
  return render_to_response('index.html')

def addScore(request,gameid):
  form = addScoreForm(request.POST)
  game = ShanghiGame.objects.all().filter(id=gameid)[0]
  player_list = ShanghiPlayer.objects.all().order_by('id')
  game.done = 0
  if form.is_valid():
    cp = game.current_player
    cr = game.current_round
    r = player_list[cp-1].rounds.all()[cr-10]
    r.singles = form.cleaned_data['singles']
    r.doubles = form.cleaned_data['doubles']
    r.triples = form.cleaned_data['triples']
    if cp == game.num_players:
      if cr == 21:
        game.done = 1
      else:
        cp = 1
        cr += 1
    else:
      cp +=1 
    game.current_player = cp
    game.current_round = cr
    game.save()
    r.save()
  matrix = []
  i=0
  while i<12:
    j=i+10
    if i == 11:
      j='B'
    matrix.append([j])
    if j == 'B': j=25
    for p in player_list:
      total = p.rounds.all()[i].singles * (j) 
      total += p.rounds.all()[i].doubles * (j) * 2
      total += p.rounds.all()[i].triples * (j) * 3
      matrix[i].append(total)
      p.total += total
    i+=1
  matrix.append(['Total'])
  for p in player_list: matrix[i].append(p.total)
  form = addScoreForm()
  return render_to_response('shanghigame.html', context_instance=RequestContext(request, {'form': form,
                                                                                    'player_list':player_list,
                                                                                     'matrix':matrix,
                                                                                     'game':game}))

def Login(request):
  form = LoginForm(request.POST)
  if form.is_valid():
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      name = user.first_name + " " + user.last_name
    else:
      name = password
  else:
    form = LoginForm()
    name = 'Guest'
  return render_to_response('login.html', context_instance=RequestContext(request, {'form':form, 'name':name}))
  
