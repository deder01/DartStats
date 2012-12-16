# Create your views here.
from django.http import HttpResponse
from django.shortcuts import *
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.core.validators import email_re
from models import *
from forms import *

def Home(request):
  return render_to_response('index.html', context_instance=RequestContext(request, {}))

def addScore(request,gameid):
  game = ShanghiGame.objects.all().filter(id=gameid)[0]
  player_list = game.players.all().order_by('player_num')
  game.done = 0
  cp = int(game.current_player)
  cr = int(game.current_round)
  justshot=game.players.all().filter(player_num=cp)[0]
  if request.method == 'POST':
    r = player_list[cp-1].rounds.all().filter(round_number=cr)[0]
    r.singles = int(request.POST['singles'])
    r.doubles = int(request.POST['doubles'])
    r.triples = int(request.POST['triples'])
    justshot.accuracy = round(((justshot.accuracy * (cr-10) * 3 + r.singles + r.doubles + r.triples) / ((cr-9) * 3)), 4)
    justshot.total += r.singles * cr + r.doubles * cr *2 + r.triples * cr * 3
    ac = justshot.accuracy
    justshot.save()
    r.save()
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
  matrix = []
  i=10
  while i<22:
    j=i
    if i == 21:
      j='B'
    matrix.append([j])
    if j == 'B': j=25
    for p in player_list:
      total = p.rounds.all().filter(round_number=i)[0].singles * (j) 
      total += p.rounds.all().filter(round_number=i)[0].doubles * (j) * 2
      total += p.rounds.all().filter(round_number=i)[0].triples * (j) * 3
      matrix[i-10].append(str(total)) 
    i+=1
  matrix.append(['Total'])
  for p in player_list: matrix[12].append(str(p.total) + " " + str(round((p.accuracy*100), 4)) + "%")
  current_player = player_list[cp-1]
  return render_to_response('shanghigame.html', context_instance=RequestContext(request, {'player_list':player_list,
                                                                                          'matrix':matrix,
                                                                                          'game':game,
                                                                                          'current_player':current_player}))

def Login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    if email_re.search(username):
      user  = User.objects.get(email=username.lower())
      if user: username = user.username
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      name = user.first_name + " " + user.last_name
    else:
      name = username 
  else:
    name = 'Guest'
  return redirect('games.views.Home')


def Logout(request):
  logout(request)
  return redirect('games.views.Home')

def Undo(request,gameid):
  game = ShanghiGame.objects.all().filter(id=gameid)[0]
  game.done = 0
  cp = int(game.current_player)
  cr = int(game.current_round)
  if cp == 1:
    cp = game.num_players
    cr = cr-1
  else:
    cp = cp-1
  redo = ShanghiPlayer.objects.all().filter(player_num=cp)[0]
  theround = redo.rounds.all().filter(round_number=cr)[0]
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

def SetUpShanghi(request):
  player_list = User.objects.all().order_by('first_name')
  return render_to_response('creategame.html', context_instance=RequestContext(request,
                                                                              {'player_list':player_list
                                                                                }))
                                                                              
def CreateShanghi(request):
  if !request.user.is_authenticated():
    return redirect(games.views.Home)
  player1 = request.POST['player1']
  player2 = request.POST['player2']
  player3 = request.POST['player3']
  player4 = request.POST['player4']
  player5 = request.POST['player5']
  name = request.POST['name']
  p1 = User.objects.all().filter(id=player1)[0]
  p2 = User.objects.all().filter(id=player2)[0]
  player_list = [p1, p2]
  if player3 != "": 
    p3 = User.objects.all().filter(id=player3)[0]
    player_list.append(p3)
  if player4 != "":
    p4 = User.objects.all().filter(id=player4)[0]
    player_list.append(p4)
  if player5 != "":
    p5 = User.objects.all().filter(id=player5)[0]
    player_list.append(p5)
  newgame = ShanghiGame(name=name, num_players=len(player_list))
  newgame.save()
  playernum=1
  for p in player_list:
    x = ShanghiPlayer(player=p, game=newgame, player_num=playernum)
    playernum += 1
    x.save()
    for i in range(0,12):
      r = ShanghiRound(round_number=i+10, shanghiplayer=x)
      r.save()
  return redirect('games.views.addScore', gameid=newgame.id)

def Stats(request):
  total_points = []
  high_score = []
  average_score=[]
  average_accuracy=[]
  total_bulls = []
  total_hits = []
  total_singles = []
  total_doubles = []
  total_triples= []
  for u in User.objects.all():
    total = 0
    highest = 0
    games = 0
    accuracy = 0.0
    bulls = 0
    singles = 0
    doubles = 0
    triples = 0
    for s in u.shanghigames.all():
      games += 1
      total += s.total
      accuracy += float(s.accuracy)
      for r in s.rounds.all():
        if r.round_number == 21:
          bulls += r.singles
          bulls += (r.doubles * 2)
        else:
          singles += r.singles
          doubles += r.doubles
          triples += r.triples
      if s.total > highest: highest = s.total
    if games == 0: games = 1
    hits = singles + doubles * 2 + triples * 3
    total_points.append([u.first_name + " " + u.last_name, total])
    high_score.append([u.first_name + " " + u.last_name, highest])
    average_accuracy.append([u.first_name + " " + u.last_name, round(float(accuracy)/float(games),4)*100])
    average_score.append([u.first_name + " " + u.last_name, round(float(total)/float(games),1)])
    total_hits.append([u.first_name + " " + u.last_name, round(float(hits)/(float(games) * 33.0),2), round(float(hits)/float(games))])
    total_bulls.append([u.first_name + " " + u.last_name, round(float(bulls)/(float(games)),1), bulls])
    total_singles.append([u.first_name + " " + u.last_name, round(float(singles)/float(games),1), singles])
    total_doubles.append([u.first_name + " " + u.last_name, round(float(doubles)/float(games),1), doubles])
    total_triples.append([u.first_name + " " + u.last_name, round(float(triples)/float(games),1), triples])
  high_score.sort(key=lambda x: x[1], reverse=True)
  total_points.sort(key=lambda x: x[1], reverse=True)
  average_score.sort(key=lambda x: x[1], reverse=True)
  average_accuracy.sort(key=lambda x: x[1], reverse=True)
  total_bulls.sort(key=lambda x: x[1], reverse=True)
  total_hits.sort(key=lambda x: x[1], reverse=True)
  total_singles.sort(key=lambda x: x[1], reverse=True)
  total_doubles.sort(key=lambda x: x[1], reverse=True)
  total_triples.sort(key=lambda x: x[1], reverse=True)
  for a in average_accuracy:
    a[1] = str(a[1]) + "%"
  return render_to_response('stats.html', context_instance=RequestContext(request, {'high_score':high_score,
                                                                                    'total_points':total_points,
                                                                                    'average_score':average_score,
                                                                                    'average_accuracy':average_accuracy,
                                                                                    'total_hits':total_hits,
                                                                                    'total_bulls':total_bulls,
                                                                                    'total_singles':total_singles,
                                                                                    'total_doubles':total_doubles,
                                                                                    'total_triples':total_triples,
                                                                                    }))
