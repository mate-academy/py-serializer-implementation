from car.models import Car
import json as js

from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return bytes(js.dumps(serializer.data, separators=(",", ":")), "utf-8")


def deserialize_car_object(json: bytes) -> Car:
    data = js.loads(json)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
    else:
        raise ValueError("Invalid data: " + str(serializer.errors))
