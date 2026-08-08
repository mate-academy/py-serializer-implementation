from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(
        required=True,
        max_length=64
    )
    model = serializers.CharField(
        required=True,
        max_length=64
    )
    horse_powers = serializers.IntegerField(
        required=True,
        min_value=1,
        max_value=1914,
    )
    is_broken = serializers.BooleanField(required=True)
    problem_description = serializers.CharField(
        required=False,
        allow_null=True
    )
