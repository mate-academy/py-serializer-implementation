from car.models import Car
import json
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data, separators=(",", ":")).encode("utf-8")


def deserialize_car_object(json_data: bytes) -> Car:
    data_dict = json.loads(json_data.decode("utf-8"))  # декодуємо bytes у str
    serializer = CarSerializer(data=data_dict)

    if serializer.is_valid(raise_exception=True):
        return serializer.save()

    print("Validation errors:", serializer.errors)
    return None

# def deserialize_car_object(data: dict):
#     data_dict = json.loads(data)
#     serializer = CarSerializer(data=data_dict)
#     if serializer.is_valid():
#         return serializer.save()
#     return serializer.errors
