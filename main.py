import json
from car.serializers import CarSerializer
from car.models import Car


def serialize_car_object(car: Car) -> bytes:
    serialized_car = CarSerializer(car).data
    result = json.dumps(serialized_car)
    return result.encode()


def deserialize_car_object(js: bytes) -> Car:
    json_string = js.decode()
    data = json.loads(json_string)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
