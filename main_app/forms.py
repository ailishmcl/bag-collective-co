import imp
from django.forms import ModelForm
from .models import Rentals

class RentalsForm(ModelForm):
    class Meta:
        model = Rentals
        fields = ['date', 'duration']
    