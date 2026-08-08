from django.urls import path
from car.views import car_list, car_detail

app_name = "car"

urlpatterns = [
    path("car/", car_list, name="car_list"),
    path("cars/<int:pk>/", car_detail, name="car_detail"),
]
