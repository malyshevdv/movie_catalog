from django import forms

class SearchActorForm(forms.Form):
    formname = forms.HiddenInput()
    search_name = forms.CharField(max_length=100, label='Name', required=False)
