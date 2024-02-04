from django import forms


class FindForm(forms.Form):
    searchstring = forms.CharField(max_length=100)