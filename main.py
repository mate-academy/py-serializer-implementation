import io
from car.models import Car
from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    steam = io.BytesIO(json)
    data_dict = JSONParser().parse(steam)
    serializer = CarSerializer(data=data_dict)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
