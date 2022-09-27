from django.urls import path

from classroom.models import Classroom, Student
from api.views import StudentListAPIView, StudentCreateAPIView, StudentRetrieveAPIView, StudentDestroyAPIView

urlpatterns = [
    path('student/list/', StudentListAPIView.as_view(), name='student_list_api'),
    path('student/create/', StudentCreateAPIView.as_view(), name='student_create_api'),
    path('student/<int:pk>/', StudentRetrieveAPIView.as_view(), name='student_detail_api'),
    path('student/<int:pk>/delete', StudentDestroyAPIView.as_view(), name='student_delete_api'),
]
