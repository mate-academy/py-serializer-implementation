from car.models import Car
from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer
import json


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json_bytes: bytes) -> Car:
    data = json.loads(json_bytes.decode("utf-8"))
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return Car(**serializer.validated_data)
