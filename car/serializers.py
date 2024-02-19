from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    horse_powers = serializers.IntegerField(required=True, validators=[
        MaxValueValidator(1914),
        MinValueValidator(1)
    ])
    is_broken = serializers.BooleanField(required=True)
    problem_description = serializers.CharField(
        required=False,
        allow_blank=True
    )
