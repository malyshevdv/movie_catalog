from django import forms


class SearchForm(forms.Form):
    formname = forms.HiddenInput
    searchstring = forms.CharField(max_length=100)




