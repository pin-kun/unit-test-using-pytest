from django.urls import path

from .models import Classroom, Student
from .views import StudentListAPIView

urlpatterns = [
    path('student/list/', StudentListAPIView.as_view(), name='student_list_api'),
]
