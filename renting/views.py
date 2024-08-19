from django.shortcuts import render
from .forms import HouseOfferForm, HouseImageForm
from .models import HouseOffer, HouseImage
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.forms import modelformset_factory


def create_offer(request):

    ImageFormSet = modelformset_factory(HouseImage,
                                        form=HouseImageForm, extra=3)
    
    if request.method == "POST":

        offer_form = HouseOfferForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=HouseImage.objects.none())

        print("OK #1")

        if offer_form.is_valid() and formset.is_valid():

            offer = offer_form.save(commit=False)
            offer.owner = request.user
            offer.save()

            print("OK #2")

            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = HouseImage(offer=offer, image=image)
                    photo.save()


            return HttpResponseRedirect(reverse("main:index"))
        else:
             print(offer_form.errors, formset.errors)

    house_form = HouseOfferForm()
    formset = ImageFormSet(queryset=HouseImage.objects.none())

    return render(request, "renting/create_offer_form.html", {"form" : house_form, 'formset': formset})


