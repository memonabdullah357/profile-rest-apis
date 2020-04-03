from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ a name field for testing our api view"""
    name = serializers.CharField(max_length=10)
