from io import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(instance=car)
    json_bytes = JSONRenderer().render(serializer.data)
    return json_bytes


def deserialize_car_object(json_bytes: bytes) -> Car:
    stream = BytesIO(json_bytes)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    car_obj = Car.objects.create(**serializer.validated_data)
    return car_obj
