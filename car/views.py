from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from car.models import Car
from car.serializers import CarSerializer


@api_view(["GET"])
def cars_list(request) -> Response:
    if request.method == "GET":
        car = Car.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def car_detail(request, pk) -> Response:
    car = get_object_or_404(Car, pk=pk)
    serializer = CarSerializer(car, context={"request": request})
    return Response(serializer.data, status.HTTP_200_OK)
