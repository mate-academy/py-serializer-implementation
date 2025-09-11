from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.FloatField(
        validators=[MinValueValidator(50), MaxValueValidator(2000)],
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        allow_null=True,
        required=False
    )
