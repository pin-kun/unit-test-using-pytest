from django.shortcuts import render
from rest_framework.generics import ListAPIView

from classroom.models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()
 