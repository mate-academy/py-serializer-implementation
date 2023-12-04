from io import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    stream = BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return Car(**serializer.validated_data)
    else:
        raise ValueError("Invalid data for deserialization")
