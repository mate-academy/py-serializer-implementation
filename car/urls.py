from django.urls import path

from car.views import cars_list

urlpatterns = [
    path("cars/", cars_list, name="car-list"),
    path("cars/<pk>/", car_detail, name="car-detailed"),
]

app_name = "car"
