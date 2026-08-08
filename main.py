from car.models import Car
from car.serializers import CarSerializer
import json as js


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return js.dumps(serializer.data, separators=(",", ":")).encode()


def deserialize_car_object(json: bytes) -> Car:
    data = js.loads(json.decode())
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
