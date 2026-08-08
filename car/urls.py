from django.urls import path

from car.views import car_list, car_detail

urlpatterns = [
    path("cars/", car_list, name="car-list"),
    path("api/car_service/cars/<int:pk>/", car_detail, name="car_detail"),
]

app_name = "car"
