from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(validators=[MaxValueValidator(1914), MinValueValidator(1)])
    is_broken = serializers.BooleanField(allow_null=False)
    problem_description = serializers.CharField(max_length=266, allow_null=True, allow_blank=True)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)
