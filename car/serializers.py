from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.PositiveSmallIntegerField(
        validators=[MaxValueValidator(1914), MinValueValidator(1)]
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.TextField(null=True, blank=True)
