from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    if isinstance(car, Car):
        serializer = CarSerializer(car)
        json = JSONRenderer().render(serializer.data)
        return json
    return TypeError


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        car = serializer.save()
        return car
    return serializer.errors
