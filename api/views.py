from tokenize import Token
from urllib import response
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication

from classroom.models import Student, Classroom
from .serializers import StudentSerializer, ClassroomSerializer

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

## Classroom model's API View
class ClassroomNumberAPIView(APIView):
    serializer_class = ClassroomSerializer
    model =  Classroom
    queryset = Classroom.objects.all()

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, *args, **kwargs):
        url_number = self.kwargs.get("student_capacity")
        print('url number:', url_number)

        classroom_qs = Classroom.objects.filter(student_capacity__lte = url_number)
        print("classroom qs--> ", classroom_qs)

        number_of_classes = classroom_qs.count()
        
        serializer = ClassroomSerializer(classroom_qs, many=True)
        return Response({"classroom_data": serializer.data, "number_of_classes": number_of_classes}, status=status.HTTP_202_ACCEPTED)
