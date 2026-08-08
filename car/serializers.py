from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField()
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        allow_blank=True, required=False
    )

    def create(self, validated_data):
        """
        Create and return a new `Car` instance, given the validated data.
        """
        return Car.objects.create(**validated_data)

    def validate_horse_powers(self, value):
        if value < 1 or value > 1914:
            raise serializers.ValidationError(
                "Horse powers must be between 1 and 1914."
            )
        return value
