# serializers.py
from rest_framework import serializers
from .models import Student, Mark

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'roll_number', 'name', 'date_of_birth']

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ['id', 'score']

