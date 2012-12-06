# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import *
from forms import *

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

  else:
    form = addScoreForm()
  matrix = []
  i=0
  while i<12:
    matrix.append([i+10])
    for p in player_list:
      total = p.rounds.all()[i].singles * (i+10) 
      total += p.rounds.all()[i].doubles * (i+10) * 2
      total += p.rounds.all()[i].triples * (i+10) * 3
      matrix[i].append(total)
    i+=1
  return render_to_response('index.html', context_instance=RequestContext(request, {'form': form,
                                                                                    'player_list':player_list,
                                                                                     'matrix':matrix,
                                                                                     'game':game}))
