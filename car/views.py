from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from car.models import Car
from car.serializers import CarSerializer


@api_view(["GET", "POST"])
def car_list(request):
    if request.method == "GET":
        movies = Car.objects.all()
        serializer = CarSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def car_detail(request, pk):
    movie = get_object_or_404(Car, pk=pk)
    if request.method == "GET":
        serializer = CarSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = CarSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
