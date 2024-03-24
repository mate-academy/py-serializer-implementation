import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    # res = bytes(json.dumps(serializer.data, separators= (',', ':')), "utf-8")
    # return res
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    res = io.BytesIO(json)
    data = JSONParser().parse(res)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
