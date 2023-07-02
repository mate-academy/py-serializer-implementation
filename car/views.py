from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from car.models import Car
from car.serializers import CarSerializer


@api_view(["GET", "POST", "PUT"])
def car_list(request):
    if request.method == "GET":
        car = Car.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(
        {"error": "Invalid request"},
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(["GET", "POST", "PUT", "DELETE"])
def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if request.method == "PUT":
        serializer = CarSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "DELETE":
        car.delete()
        return Response(
            {"message": "Car deleted"},
            status=status.HTTP_204_NO_CONTENT
        )

    serializer = CarSerializer(car)
    return Response(serializer.data)
