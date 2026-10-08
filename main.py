from car.models import Car
from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    data = io.BytesIO(json)
    json_data = JSONParser().parse(data)
    serializer = CarSerializer(data=json_data)
    if serializer.is_valid():
        return serializer.save()
