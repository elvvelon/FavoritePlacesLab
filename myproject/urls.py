from django.urls import path
from myproject import views

urlpatterns = [
    path("", views.home, name="home"),
    path("places", views.places_list, name="places_list"),
    path("places/<int:place_id>", views.place_detail, name="place_detail"),
    path("places/add", views.place_add, name="place_add"),
]