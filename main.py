import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json = JSONRenderer().render(serializer.data)
    return json


def deserialize_car_object(car_json: str) -> Car:
    if isinstance(car_json, str):
        car_json = car_json.encode("utf-8")
    stream = io.BytesIO(car_json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)

    if serializer.is_valid():
        return serializer.create(serializer.validated_data)
    else:
        raise ValueError(f"Invalid data for Car object: {serializer.errors}")
