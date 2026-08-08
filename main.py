from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io


def serialize_car_object(car):
    serializer = CarSerializer(car)
    content = JSONRenderer().render(serializer.data)
    return content


def deserialize_car_object(json_data):
    stream = io.BytesIO(json_data)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
