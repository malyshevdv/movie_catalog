from django import forms


class ActionForm(forms.Form):
    MyId = forms.DecimalField(decimal_places=0, max_digits=10)
    Action = forms.CharField(max_length=50, required=False)
    FormName = forms.CharField(max_length=50, required=False)