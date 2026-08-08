from django.urls import path

from car.views import car_list

urlpatterns = [
    path("cars/", car_list, name="car-list"),
]

app_name = "car"
