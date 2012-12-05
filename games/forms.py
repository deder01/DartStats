from django import forms

class addTenForm(forms.Form):
  tens = forms.IntegerField()

