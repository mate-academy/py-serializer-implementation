import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from car.serializers import CarSerializer


def serialize_car_object(car):
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json_data):
    if isinstance(json_data, dict):
        data = json_data
    else:
        if isinstance(json_data, str):
            json_data = json_data.encode("utf-8")

        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)

    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
