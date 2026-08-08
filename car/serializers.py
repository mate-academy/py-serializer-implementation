from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    pass
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1914)
        ]
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        required=False,
        allow_null=True
    )
