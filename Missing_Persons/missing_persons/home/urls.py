# Authors: Tanner Child, Cameron Pennock, Dawson Newell, Evan Neff, Jake Millett, Paxton Davis
# The purpose of this application is to raise awareness of Human traffiking and to create a website displaying 
# the data of missing persons.

from django.urls import path
from .views import indexPageView, aboutView, contView, personView

urlpatterns = [
    path("", indexPageView, name="Index"),
    path("about/", aboutView, name="About"),
    path("contributions/", contView, name="Contributions"),
    path("<int:id>", personView, name="MissingPerson")
]
