from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from car.models import Car
from car.serializers import CarSerializer


@api_view(["GET", "POST"])
def car_list(request):
    if request.method == "GET":
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == "GET":
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = CarSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
