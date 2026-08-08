import json
from rest_framework.renderers import JSONRenderer
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json_bytes: bytes) -> Car:
    json_string = json_bytes.decode("utf-8")
    json_data = json.loads(json_string)
    serializer = CarSerializer(data=json_data)

    serializer.is_valid(raise_exception=True)
    new_car = serializer.save()
    return new_car
