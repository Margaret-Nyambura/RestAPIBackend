from rest_framework import serializers
from student.models import Student
from clases.models import Classes
from class_period.models import ClassPeriod
from course.models import Courses
from teacher.models import Teacher
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = "__all__"
class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = "__all__"
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
