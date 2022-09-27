from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView

from classroom.models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()

class StudentCreateAPIView(CreateAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()

class StudentRetrieveAPIView(RetrieveAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()

class StudentDestroyAPIView(DestroyAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()
