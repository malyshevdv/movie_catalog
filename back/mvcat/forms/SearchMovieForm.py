from django import forms

class SearchMovieForm(forms.Form):
    formname = forms.HiddenInput()
    search_title = forms.CharField(max_length=100, label='title', required=False)
    search_year =  forms.DecimalField(max_digits=4, decimal_places=0, label='year', required=False)
    search_description = forms.CharField(max_length=100, label='Descriptionr', required=False)
    search_country = forms.CharField(max_length=100, label='Country', required=False)

    search_actor = forms.CharField(max_length=100, label='Actor', required=False)
    search_actor_list = forms.BooleanField(label='Use actor list', required=False)
    search_actor_colaboration = forms.BooleanField(label='Colaboration', help_text='Actors work together in some movies', required=False)


    search_have_poster = forms.BooleanField(label='Have poster', required=False)
