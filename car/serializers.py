from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(min_value=100, max_value=300)
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(required=False)
