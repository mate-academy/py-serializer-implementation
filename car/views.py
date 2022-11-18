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
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = CarSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def car_detail(request, pk):
    try:
        cars = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        cars = Car.objects.filter(pk=pk)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = CarSerializer(cars, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        cars.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
