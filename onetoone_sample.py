import os
from django import setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
setup()

from ModelApp.models import Places, Restaurants

places = [
    ('Motomachi','Yokohama'), ('Tukiji','Tokyo')
]
restaurants = ['restaurant1','restaurant2']

for place_name, place_address in places:
    p =Places(name=place_name, address=place_address)
    p.save()
    for restaurants_name in restaurants:
        # r = Restaurants(place=p, name=restaurants_name)
        # r.save()
        Restaurants.objects.create(
            place=p, name=restaurants_name
        )
