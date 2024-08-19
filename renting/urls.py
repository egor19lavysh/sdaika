from django.urls import path
from . import views

app_name = "renting"

urlpatterns = [
    path("create/", view=views.create_offer, name="create_offer"),
]
