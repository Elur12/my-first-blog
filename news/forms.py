from django import forms

from .models import Town, zakaz

class TownForm(forms.ModelForm):

    class Meta:
        model = Town
        fields = ('name', 'text', 'coord')
class ZakazForm(forms.ModelForm):

    class Meta:
        model = zakaz
        fields = ('YouTown', 'ArrivalTown', 'Nick_Recipient', 'You_Nick')