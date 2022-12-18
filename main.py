from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    porsche = Car.objects.create(
        manufacturer="Porsche",
        model="Cayenne",
        horse_powers=434,
        is_broken=False,
    )
    serializer = CarSerializer(porsche)
    json = JSONRenderer().render(serializer.data)
    return json


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return serializer.validated_data
