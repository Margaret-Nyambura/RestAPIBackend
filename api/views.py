from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import  StudentSerializer
from clases.models import Classes
from .serializers import  ClassesSerializer
from class_period.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from course.models import Courses
from .serializers import CoursesSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from rest_framework import status

class StudentListView(APIView):
    def get(self,  request):
        Students = Student.objects.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class StudentDetailView(APIView):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)   
    
    def put(self, request, id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
                
    
    
class ClassesListView(APIView):
    def get(self,  request):
        classes = Classes.objects.all()
        serializer = ClassesSerializer(classes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassesSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ClassDetailView(APIView):
    def get(self, request, id):
        classes = Classes.objects.get(id=id)
        serializer = ClassesSerializer(classes)
        return Response(serializer.data)
    
    def put(self, request, id):
        classes = Classes.objects.get(id=id)
        serializer = ClassesSerializer(classes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        classes = Classes.objects.get(id=id)
        classes.delete()
        return Response(status=status.HTTP_202_ACCEPTED)  
    
    
    
    
class ClassPeriodListView(APIView):
    def get(self, request):
        ClassPeriod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(ClassPeriod, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassPeriodSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(class_period)
        return Response(serializer.data)
    
    def put(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(class_period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        class_period.delete()
        return Response(status=status.HTTP_202_ACCEPTED)      
    
    
    
class CoursesListView(APIView):
    def get(self, request):
        Courses = Courses.objects.all()
        serializer = CoursesSerializer(Courses, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CoursesSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class CoursesDetailView(APIView):
    def get(self, request, id):
        course = Courses.objects.get(id=id)
        serializer = CoursesSerializer(course)
        return Response(serializer.data) 
    
    def put(self, request, id):
        course = Courses.objects.get(id = id)
        serializer = CoursesSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
             
    def delete(self, request, id):
        course = Courses.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
                
    
    
class TeacherListView(APIView):
    def get(self, request):
        Teacher = Teacher.objects.all()
        serializer = TeacherSerializer(Teacher, many = True)
        return Response(serializer.data)


    def post(self, request):
        serializer = TeacherSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data) 
    
    def put(self, request, id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
             
    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
