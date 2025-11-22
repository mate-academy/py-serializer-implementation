from django.urls import path

from car.views import deserialize_car_object
from car.views import serialize_car_object


app_name = "car"
urlpatterns = [
    path(
        "serialize_car_object/<int:car_id>",
        serialize_car_object,
        name="serialize-car"
    ),
    path(
        "deserialize_car_object",
        deserialize_car_object,
        name="deserialize-car"
    ),
]
