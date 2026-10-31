from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    manufacturer = serializers.CharField(max_length=64, required=True)
    model = serializers.CharField(max_length=64, required=True)
    horse_powers = serializers.IntegerField(
        required=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1999)
        ]
    )
    is_broken = serializers.BooleanField(required=True)
    problem_description = serializers.CharField(
        required=False,
        allow_blank=True
    )
