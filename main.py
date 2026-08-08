from car.models import Car
import io
from rest_framework.renderers import JSONRenderer
from car.serializers import CarSerializer
from rest_framework.parsers import JSONParser


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    data = serializer.data
    json_data = JSONRenderer().render(data)
    return json_data


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        car = serializer.save()
        return car
