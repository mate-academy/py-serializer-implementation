# # Create your views here.
# from car.models import Car
# from car.serializers import CarSerializer
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
#
# class CarList(APIView):
#     def get(self, request):
#         cars = Car.objects.all()
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = CarSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors,
#         status=status.HTTP_400_BAD_REQUEST)
#
#
# class CarDetail(APIView):
#     pass
