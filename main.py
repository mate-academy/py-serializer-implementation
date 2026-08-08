import io

from car.models import Car
from car.serializers import CarSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


def serialize_car_object(car: Car):
    serializer = CarSerializer(car)
    json_file = JSONRenderer().render(serializer.data)
    return json_file


def deserialize_car_object(json_data: bytes) -> Car:
    stream = io.BytesIO(json_data)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
