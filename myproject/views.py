import random
from django.shortcuts import render, get_object_or_404, redirect
from myproject.models import Place

def get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def home(request):
    session_key = get_session_key(request)
    places = Place.objects.filter(session_key=session_key)
    random_place = None

    if request.GET.get('random') == 'true' and places.exists():
        weights = [place.rating for place in places]
        random_place = random.choices(list(places), weights=weights, k=1)[0]

    return

def places_list(request):
    session_key = get_session_key(request)
    places = Place.objects.filter(session_key=session_key).order_by('-created_at')
    return

def place_detail(request, place_id):
    session_key = get_session_key(request)
    place = get_object_or_404(Place, pk=place_id, session_key=session_key)
    return

def place_add(request):
    session_key = get_session_key(request)
    return
