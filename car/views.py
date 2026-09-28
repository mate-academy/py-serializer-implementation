from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from car.serializers import CarSerializer


class CarSerializersView(APIView):
    parser_classes = [JSONParser]

    def post(self, request, format=None) -> Response:
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)


class CarDeserializersView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request, format=None) -> Response:
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        car_instance = serializer.save()
        return Response(CarSerializer(car_instance).data,
                        status=status.HTTP_201_CREATED)
