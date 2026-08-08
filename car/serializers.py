from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        validators=[
            MinValueValidator(50),
            MaxValueValidator(1500)
        ]
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        allow_null=True,
        required=False
    )
