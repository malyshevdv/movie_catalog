from django import forms


class AddActorToCompareForm(forms.Form):
    id = forms.DecimalField(decimal_places=0, max_digits=10)
    FormName = forms.CharField(max_length=50, required=False)
