# Authors: Tanner Child, Cameron Pennock, Dawson Newell, Evan Neff, Jake Millett, Paxton Davis
# The purpose of this application is to raise awareness of Human traffiking and to create a website displaying 
# the data of missing persons.

from django.contrib import admin
from .models import MissingPersons

admin.site.register(MissingPersons)
