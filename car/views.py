from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from .serializers import CarSerializer


@api_view(["GET"])
def get_car(request, car_id):
    """
    Возвращает JSON для объекта Car по его ID.
    """
    try:
        car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        return Response(
            {"error": "Car not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = CarSerializer(car)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_car(request):
    """
    Принимает JSON и создает объект Car.
    """
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        car = serializer.save()
        return Response(
            CarSerializer(car).data,
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
