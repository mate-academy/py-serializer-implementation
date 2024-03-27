from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            "id",
            "manufacturer",
            "model",
            "horse_powers",
            "is_broken",
            "problem_description",
        ]
        read_only_fields = ["id"]
