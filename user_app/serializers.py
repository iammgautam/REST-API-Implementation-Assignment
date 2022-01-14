from rest_framework import serializers
from .models import User

class WriteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "company_name",
            "city",
            "state",
            "zip",
            "email",
            "web",
            "age"
        ) 

class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "company_name",
            "city",
            "state",
            "zip",
            "email",
            "web",
            "age"
        )
        read_only_fields = fields
            