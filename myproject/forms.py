from django import forms
from myproject.models import Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'description', 'place_type', 'address', 'rating']