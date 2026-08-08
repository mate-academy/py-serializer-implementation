from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64, required=True)
    model = serializers.CharField(max_length=64, required=True)
    horse_powers = serializers.IntegerField(
        min_value=1,
        max_value=1914,
        required=True,
    )
    is_broken = serializers.BooleanField(default=False)
    problem_description = serializers.CharField(required=False)
