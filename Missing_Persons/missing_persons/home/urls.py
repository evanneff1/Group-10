from django.urls import path
from .views import indexPageView, aboutView

urlpatterns = [
    path("", indexPageView, name="Index"),
    path("about", aboutView, name="About"),
]
