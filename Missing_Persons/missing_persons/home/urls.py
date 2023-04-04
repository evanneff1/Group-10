from django.urls import path
from .views import indexPageView, aboutView, contView

urlpatterns = [
    path("", indexPageView, name="Index"),
    path("about", aboutView, name="About"),
    path("contributions", contView, name="Contributions"),
]
