from django import forms

class DeleteSelectedActorForm(forms.Form):
    ItemId = forms.DecimalField(decimal_places=0, max_digits=10, required=False)
    FormName = forms.CharField(max_length=50)

