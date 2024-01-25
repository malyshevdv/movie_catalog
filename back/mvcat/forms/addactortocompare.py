from django import forms


class AddActorToCompare(forms.Form):
    id = forms.DecimalField(decimal_places=0, max_digits=10)
