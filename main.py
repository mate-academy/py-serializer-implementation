import json
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_str = json.dumps(serializer.data, separators=(",", ":"))
    return json_str.encode("utf-8")


def deserialize_car_object(json_bytes: bytes) -> Car:
    data = json.loads(json_bytes.decode("utf-8"))
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    result = serializer.save()
    if isinstance(result, list):
        # If a list is returned, get the first Car object or handle as needed
        return result[0]
    return result
