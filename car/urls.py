from django.urls import path

from car.views import car_list, car_detail

urlpatterns = [
    path("cars/", car_list, name="car-list"),
    path("cars/", car_detail, name="car-detail"),
]

app_name = "car"