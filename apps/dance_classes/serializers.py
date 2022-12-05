from rest_framework import serializers

from .models import DanceClass


class DanceClassSerializer(serializers.ModelSerializer):
    """
    Validates and converts request data into Python types.
    """

    class Meta:
        model = DanceClass
        fields = (
            "teacher",
            "location",
            "date",
        )
