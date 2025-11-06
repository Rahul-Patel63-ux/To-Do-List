from rest_framework import serializers
from .models import ToDoList
from django.contrib.auth.models import User

class TasksSerializer(serializers.ModelSerializer):
    # created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
    class Meta:
        model = ToDoList
        fields = "__all__"
        read_only_fields = ['created_at']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'date_joined')
        


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user
