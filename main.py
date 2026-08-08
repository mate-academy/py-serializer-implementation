import json as js

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(instance=car)
    return js.dumps(
        serializer.data,
        separators=(",", ":")
    ).encode("utf-8")


def deserialize_car_object(json: bytes) -> Car:
    json_str = json.decode("utf-8")
    data = js.loads(json_str)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return Car.objects.create(**serializer.validated_data)
