# Create your views here.
from django.http import HttpResponse
from django.shortcuts import *
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.core.validators import email_re
from models import *
from forms import *
from operator import itemgetter

def Home(request):
  return render_to_response('index.html', context_instance=RequestContext(request, {}))

def addScore(request,gameid):
  game = ShanghiGame.objects.all().filter(id=gameid)[0]
  player_list = game.players.all().order_by('player_number')
  cp = int(game.current_player)
  cr = int(game.current_round)
  justshot=game.players.all().filter(player_number=cp)[0]
  error_message = ""
  if request.method == 'POST' and not game.done:
    thisround = player_list[cp-1].rounds.all().filter(round_number=cr)[0]
    thisround.singles = int(request.POST['singles'])
    thisround.doubles = int(request.POST['doubles'])
    thisround.triples = int(request.POST['triples'])
    if (thisround.singles + thisround.doubles + thisround.triples) > 3:
      error_message = "You submitted a score that would require throwing more than three darts.  Please try again."
    else:
      if thisround.singles == 1 and thisround.doubles == 1 and thisround.triples == 1:
        game.done = True
        game.shanghiwin = True
        game.winner = justshot.player
      justshot.accuracy = round(((justshot.accuracy * (cr-10) * 3 + thisround.singles + thisround.doubles + thisround.triples)
                                  / ((cr-9) * 3)), 4)
      justshot.total += thisround.singles * cr + thisround.doubles * cr *2 + thisround.triples * cr * 3
      justshot.save()
      thisround.save()
      if cp == game.num_players:
        if cr > 20:
          game.done = True
          highest = 0
          for p in player_list:
            if p.total > highest:
              highest = p.total
              game.winner = p.player
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
  return render_to_response('shanghigame.html', context_instance=RequestContext(request, 
                                                                                {'player_list':player_list,
                                                                                 'matrix':matrix,
                                                                                 'game':game,
                                                                                 'current_player':current_player,
                                                                                 'error_message':error_message}))

def Login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    if email_re.search(username):
      user  = Usethisround.objects.get(email=username.lower())
      if user: username = usethisround.username
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      name = usethisround.first_name + " " + usethisround.last_name[0] + "."
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
  game.done = False
  game.shanghi = False
  cp = int(game.current_player)
  cr = int(game.current_round)
  if cp == 1:
    cp = game.num_players
    cr = cr-1
  else:
    cp = cp-1
  redo = game.players.all().filter(player_number=cp)[0]
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
  if request.usethisround.is_authenticated() == False:
    return render_to_response('notloggedin.html', context_instance=RequestContext(request, {})) 
  player_list = Usethisround.objects.all().order_by('first_name')
  return render_to_response('creategame.html', context_instance=RequestContext(request,
                                                                              {'player_list':player_list
                                                                                }))
                                                                              
def CreateShanghi(request):
  player1 = request.POST['player1']
  player2 = request.POST['player2']
  player3 = request.POST['player3']
  player4 = request.POST['player4']
  player5 = request.POST['player5']
  name = request.POST['name']
  p1 = Usethisround.objects.all().filter(id=player1)[0]
  p2 = Usethisround.objects.all().filter(id=player2)[0]
  player_list = [p1, p2]
  if player3 != "": 
    p3 = Usethisround.objects.all().filter(id=player3)[0]
    player_list.append(p3)
  if player4 != "":
    p4 = Usethisround.objects.all().filter(id=player4)[0]
    player_list.append(p4)
  if player5 != "":
    p5 = Usethisround.objects.all().filter(id=player5)[0]
    player_list.append(p5)
  newgame = ShanghiGame(name=name, num_players=len(player_list))
  newgame.save()
  playernum=1
  for p in player_list:
    x = ShanghiPlayer(player=p, game=newgame, player_number=playernum)
    playernum += 1
    x.save()
    for i in range(0,12):
      r = ShanghiRound(round_number=i+10, shanghiplayer=x)
      thisround.save()
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
  total_wins = []
  for u in thisround.objects.all():
    total = 0
    highest = 0
    accuracy = 0.0
    bulls = 0
    singles = 0
    doubles = 0
    triples = 0
    for s in u.shanghigames.all():
      if not s.game.shanghiwin:
        total += s.total
        accuracy += float(s.accuracy)
      for r in s.rounds.all():
        if thisround.round_number == 21:
          bulls += thisround.singles
          bulls += (thisround.doubles * 2)
        else:
          singles += thisround.singles
          doubles += thisround.doubles
          triples += thisround.triples
      if s.total > highest and not s.game.shanghiwin: highest = s.total
    hits = singles + doubles * 2 + triples * 3
    wins = len(u.shanghigames_won.all())
    games = len(u.shanghigames.all())
    loses = games - wins
    if games == 0: games = 1
    total_points.append([u.first_name + " " + u.last_name[0] + ".", total])
    high_score.append([u.first_name + " " + u.last_name[0] + ".", highest])
    average_accuracy.append([u.first_name + " " + u.last_name[0] + ".", round(float(accuracy)/float(games),4)*100])
    average_score.append([u.first_name + " " + u.last_name[0] + ".", round(float(total)/float(games),1)])
    total_hits.append([u.first_name + " " + u.last_name[0] + ".", round(float(hits)/(float(games) * 33.0),2), round(float(hits)/float(games))])
    total_bulls.append([u.first_name + " " + u.last_name[0] + ".", round(float(bulls)/(float(games)),1), bulls])
    total_singles.append([u.first_name + " " + u.last_name[0] + ".", round(float(singles)/float(games),1), singles])
    total_doubles.append([u.first_name + " " + u.last_name[0] + ".", round(float(doubles)/float(games),1), doubles])
    total_triples.append([u.first_name + " " + u.last_name[0] + ".", round(float(triples)/float(games),1), triples])
    total_wins.append([u.first_name + " " + u.last_name[0] + ".", wins+loses, round(float(wins)/float(games), 4) * 100, wins, loses])

  high_score.sort(key=itemgetter(1, 0), reverse=True)
  total_points.sort(key=itemgetter(1, 0), reverse=True)
  average_score.sort(key=itemgetter(1, 0), reverse=True)
  average_accuracy.sort(key=itemgetter(1, 0), reverse=True)
  total_bulls.sort(key=itemgetter(1, 0), reverse=True)
  total_hits.sort(key=itemgetter(1, 0), reverse=True)
  total_singles.sort(key=itemgetter(1, 0), reverse=True)
  total_doubles.sort(key=itemgetter(1, 0), reverse=True)
  total_triples.sort(key=itemgetter(1, 0), reverse=True)
  total_wins.sort(key=itemgetter(0))
  total_wins.sort(key=itemgetter(2, 1, 3, 4), reverse=True)
  for a in average_accuracy:
    a[1] = str(a[1]) + "%"
  for w in total_wins:
    w[2] = str(w[2]) + "%"
  return render_to_response('stats.html', context_instance=RequestContext(request, {'high_score':high_score,
                                                                                    'total_points':total_points,
                                                                                    'average_score':average_score,
                                                                                    'average_accuracy':average_accuracy,
                                                                                    'total_hits':total_hits,
                                                                                    'total_bulls':total_bulls,
                                                                                    'total_singles':total_singles,
                                                                                    'total_doubles':total_doubles,
                                                                                    'total_triples':total_triples,
                                                                                    'total_wins':total_wins,
                                                                                    }))

def History(request):
  all_games = ShanghiGame.objects.all().order_by('-id')
  return render_to_response('history.html', context_instance=RequestContext(request, {'all_games':all_games,
                                                                                      }))
