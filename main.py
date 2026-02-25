from car.models import Car
from car.serializers import CarSerializer
from rest_framework.parsers import JSONParser
from io import BytesIO
from rest_framework.renderers import JSONRenderer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_bytes = JSONRenderer().render(serializer.data)
    return json_bytes


def deserialize_car_object(json: bytes) -> Car:
    bits = BytesIO(json)
    data = JSONParser().parse(bits)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    car = serializer.save()
    return car
