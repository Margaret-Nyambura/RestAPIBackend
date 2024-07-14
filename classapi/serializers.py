from rest_framework import serializers
from student.models import Student
from classperiod.models import ClassPeriod

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class ClassPeriod(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = "__all__"