# Create your views here.
from django.http import HttpResponse
from django.shortcuts import *
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout
from models import *
from forms import *

def Home(request):
  return render_to_response('index.html', context_instance=RequestContext(request, {}))

def addScore(request,gameid):
  game = ShanghiGame.objects.all().filter(id=gameid)[0]
  player_list = ShanghiPlayer.objects.all().order_by('id')
  game.done = 0
  cp = int(game.current_player)
  cr = int(game.current_round)
  justshot=ShanghiPlayer.objects.all()[cp-1]
  if request.method == 'POST':
    r = player_list[cp-1].rounds.all()[cr-10]
    r.singles = int(request.POST['singles'])
    r.doubles = int(request.POST['doubles'])
    r.triples = int(request.POST['triples'])
    justshot.accuracy = round(((justshot.accuracy * (cr-10) * 3 + r.singles + r.doubles + r.triples) / ((cr-9) * 3)), 4)
    justshot.total += r.singles * cr + r.doubles * cr *2 + r.triples * cr * 3
    justshot.save()
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
      matrix[i].append(str(total)) 
    i+=1
  matrix.append(['Total'])
  for p in player_list: matrix[i].append(str(p.total) + " " + str(round((p.accuracy*100), 2)) + "%")
  current_player = player_list[cp-1]
  return render_to_response('shanghigame.html', context_instance=RequestContext(request, {'player_list':player_list,
                                                                                          'matrix':matrix,
                                                                                          'game':game,
                                                                                          'current_player':current_player}))

def Login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      name = user.first_name + " " + user.last_name
    else:
      name = username 
  else:
    name = 'Guest'
  return render_to_response('login.html', context_instance=RequestContext(request))


def Logout(request):
  logout(request)
  return redirect('games.views.Home')

def Undo(request,gameid):
  game = ShanghiGame.objects.all().filter(id=gameid)[0]
  player_list = ShanghiPlayer.objects.all().order_by('id')
  game.done = 0
  cp = int(game.current_player)
  cr = int(game.current_round)
  if cp == 1:
    cp = game.num_players
    cr = cr-1
  else:
    cp = cp-1
  redo = player_list[cp-1]
  theround = redo.rounds.all()[cr-10]
  if cr == 10:
    redo.accuracy = 0
    redo.total=0
  else:
    redo.accuracy = round((redo.accuracy * (cr-9) * 3 - theround.singles - theround.doubles - theround.triples) / ((cr-10) * 3),4)
    redo.total = redo.total - (theround.singles * cr) - (theround.doubles * 2 * cr) - (theround.triples * 3 * cr)
  theround.singles=0
  theround.doubles=0
  theround.triples=0
  game.current_round = cr
  game.current_player = cp
  redo.save()
  theround.save()
  game.save()
  return redirect('games.views.addScore', gameid=gameid)
