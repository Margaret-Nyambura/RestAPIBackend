from django.urls import path, include
from .views      import StudentListView, ClassesListView, ClassPeriodListView, CoursesListView, TeacherListView, StudentDetailView, ClassDetailView, ClassPeriodDetailView, CoursesDetailView, TeacherDetailView 
urlpatterns = [
    path('student/', StudentListView.as_view(), name = 'student_list_view') ,
    path('clases/', ClassesListView.as_view(), name = 'classes_list_view'),
    path('class_period/', ClassPeriodListView.as_view(), name = 'classperiod_list_view'),
    path('courses/', CoursesListView.as_view(), name = 'courses_list_view'),
    path('classperiod/', TeacherListView.as_view(), name = 'teacher_list_view'),
    path('student,', StudentDetailView.as_view(), name = 'student_detail_view'),
    path('classes', ClassDetailView.as_view(), name = 'class_detail_view'),
    path('class_period', ClassPeriodDetailView.as_view(), name = 'class_period_detail_view'),
    path('course', CoursesDetailView.as_view(), name = 'courses_detail_view'),
    path('teacher', TeacherDetailView.as_view(), name = 'teacher_detail_view'),
]