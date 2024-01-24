from django import forms
from .models import Country, Actor, MovieType
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class YearInSchool(models.TextChoices):
    FRESHMAN = "FR", _("Freshman")
    SOPHOMORE = "SO", _("Sophomore")
    JUNIOR = "JR", _("Junior")
    SENIOR = "SR", _("Senior")
    GRADUATE = "GR", _("Graduate")


class PhoneField(forms.MultiValueField):
    def __init__(self, **kwargs):
        # Define one message for all fields.
        error_messages = {
            "incomplete": "Enter a country calling code and a phone number.",
        }
        # Or define a different message for each field.
        fields = (
            forms.CharField(
                error_messages={"incomplete": "Enter a country calling code."},
                validators=[
                    RegexValidator(r"^[0-9]+$", "Enter a valid country calling code."),
                ],
            ),
            forms.CharField(
                error_messages={"incomplete": "Enter a phone number."},
                validators=[RegexValidator(r"^[0-9]+$", "Enter a valid phone number.")],
            ),
            forms.CharField(
                validators=[RegexValidator(r"^[0-9]+$", "Enter a valid extension.")],
                required=False,
            ),
        )
        super().__init__(
            error_messages=error_messages,
            fields=fields,
            require_all_fields=False,
            **kwargs
        )


class LoadMoviesFromFile(forms.Form):
    #name = forms.CharField(max_length=20)
    movietype = forms.ModelChoiceField(queryset=MovieType.objects.all(), empty_label="(Nothing)")
    myFile = forms.FileField()
    def get_context(self, *args, **kwargs):
        cont = super().get_context(*args, **kwargs)
        return cont
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MyForm(forms.Form):
    name = forms.CharField(max_length=20)
    birthday = forms.DateField(input_formats="%Y-%m-%d")
    birthday2 = forms.SplitDateTimeField()
    actor = forms.ModelChoiceField(queryset=None)
    field1 = forms.ModelChoiceField(queryset=Actor.objects.all(), empty_label="(Nothing)")

    price = forms.DecimalField(decimal_places=2, max_digits=15)
    capacity = forms.DecimalField(decimal_places=3, max_digits=15)
    duration = forms.DurationField()
    myFile = forms.FileField()
    #myPath = forms.FilePathField(allow_folders=False, allow_files=True)

    #mypassword = forms.PasswordInput()

    myChoices = []

    for item in Country.objects.all():
        myChoices.append((item.id, item.name))

    stat = forms.ChoiceField(choices=tuple(myChoices))

    myListChoice = forms.MultipleChoiceField(choices=tuple(myChoices))

    myBool = forms.NullBooleanField()
    myTyped = forms.TypedChoiceField(choices=tuple(myChoices))
    f = forms.ComboField(fields=[forms.CharField(max_length=20), forms.EmailField()])
    phone_number= PhoneField()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["actor"].queryset = Actor.objects.all()
class CountrySelect(forms.Select):
    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option = super().create_option(
            name, value, label, selected, index, subindex, attrs
        )
        #if value:
        #    option["attrs"]["data-price"] = value.instance.price
        return option


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ["country"]
        widgets = {"country": CountrySelect}