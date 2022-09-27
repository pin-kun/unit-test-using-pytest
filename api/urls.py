from django.urls import path

from classroom.models import Classroom, Student
from api.views import StudentListAPIView

urlpatterns = [
    path('student/list/', StudentListAPIView.as_view(), name='student_list_api'),
]
