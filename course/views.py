from django.shortcuts import render
from .forms import CourseRegistrationForm
# Create your views here.
def register_course(request):
    form = CourseRegistrationForm()
    return render(request, "course/register_course.html",
                  {"form": form})