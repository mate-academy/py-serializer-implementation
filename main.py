from car.models import Car
from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from io import BytesIO


def serialize_car_object(car: Car) -> bytes:
    serializer_data = CarSerializer(car).data
    json = JSONRenderer().render(serializer_data)
    return json


def deserialize_car_object(json: bytes) -> Car:
    stream = BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return Car(**serializer.validated_data)
