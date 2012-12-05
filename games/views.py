# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import *
from forms import *

def addTen(request):
  form = addTenForm(request.POST)
  if form.is_valid():
    p1 = ShanghiPlayer.objects.all()[0]
    p1.ten = p1.ten + form.cleaned_data['tens']
    p1.save()
  else:
    form = addTenForm()
  player_list = ShanghiPlayer.objects.all().order_by('id')
  return render_to_response('index.html', context_instance=RequestContext(request, {'form': form, 'player_list':player_list}))
