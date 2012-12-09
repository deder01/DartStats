from django import forms

class addScoreForm(forms.Form):
  singles = forms.IntegerField(initial=0)
  doubles = forms.IntegerField(initial=0)
  triples = forms.IntegerField(initial=0)

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=100)
