from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(max_value=1914, min_value=1)
    is_broken = serializers.BooleanField(default=False)
    problem_description = serializers.CharField(required=False)
