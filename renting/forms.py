from .models import HouseOffer, HouseImage
from django import forms

class HouseOfferForm(forms.ModelForm):

    class Meta:
        model=HouseOffer
        #fields=["title", "description", "category", "price", "guests", "bedrooms", "bathrooms", "location", "amenities", ]
        exclude=["owner", "created_at", "updated_at"]

class HouseImageForm(forms.ModelForm):
    image = forms.ImageField(label="images")

    class Meta:
        fields = ('image',)
