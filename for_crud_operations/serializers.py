from . models import *
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Name must be at least 3 characters.")
        elif not value[0].isupper():
            raise serializers.ValidationError("Name must Start with Upper case.")
        else:
            return value
    
    def validate_age(self, value):
        if value > 61:
            raise serializers.ValidationError("Age must be less than 60.")
        elif value < 18:
            raise serializers.ValidationError("Age must be greater than 18.")
        else:
            return value