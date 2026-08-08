from car.models import Car
from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser


def serialize_car_object(car: Car) -> bytes:
    serialized_car = CarSerializer(car).data
    return JSONRenderer().render(serialized_car)


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    car = Car(**data)
    return car
