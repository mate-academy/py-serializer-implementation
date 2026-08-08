from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    variable_with_dict = io.BytesIO(json)
    data = JSONParser().parse(variable_with_dict)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return Car.objects.create(**serializer.validated_data)
