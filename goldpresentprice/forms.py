# goldpresentprice/forms.py

from django import forms
from .models import GoldPrice

class GoldPriceForm(forms.ModelForm):
    class Meta:
        model = GoldPrice
        fields = ['date']
