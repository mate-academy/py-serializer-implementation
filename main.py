import io
from rest_framework.parsers import JSONParser
from car.models import Car
from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    res = JSONRenderer().render(serializer.data)
    return res


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return serializer.validated_data
