from django.http import JsonResponse
from car.serializers import CarSerializer
from car.models import Car

def serialize_car_object(car: Car):
    serializer = CarSerializer(instance=car)
    return JsonResponse(serializer.data)


def deserialize_car_object(data):
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
    print("Deserialization failed:", serializer.errors)
    return None
