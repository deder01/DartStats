from django import forms

class addScoreForm(forms.Form):
  singles = forms.IntegerField()
  doubles = forms.IntegerField()
  triples = forms.IntegerField()

