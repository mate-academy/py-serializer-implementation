from json import loads, dumps

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return dumps(serializer.data, separators=(",", ":")).encode("utf-8")


def deserialize_car_object(json: bytes) -> Car:
    data = loads(json.decode("utf-8"))
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        car = serializer.save()
        return car
