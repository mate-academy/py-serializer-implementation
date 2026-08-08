from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField()
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        allow_null=True, required=False
    )

    def validate_horse_powers(self, value):
        if value < 1 or value > 1914:
            raise serializers.ValidationError(
                "Horse power must be between 1 and 1914."
            )
        return value
