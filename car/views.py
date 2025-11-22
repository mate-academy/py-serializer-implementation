from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from car.models import Car
from car.serializers import CarSerializer


@api_view(["GET"])
def serialize_car_object(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    serializer = CarSerializer(car)
    return Response(serializer.data)


@api_view(["POST"])
def deserialize_car_object(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
