from django import forms

class addScoreForm(forms.Form):
  singles = forms.IntegerField(initial=0)
  doubles = forms.IntegerField(initial=0)
  triples = forms.IntegerField(initial=0)

