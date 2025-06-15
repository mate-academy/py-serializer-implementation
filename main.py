from io import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from car.serializers import CarSerializer
from car.models import Car


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json = JSONRenderer().render(serializer.data)
    return json


def deserialize_car_object(json: bytes) -> Car:
    data = JSONParser().parse(BytesIO(json))
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Car(**serializer.data)
