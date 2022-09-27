from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from classroom.models import Student, Classroom


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('last_name', 'username', 'admission_number', 'is_qualified', )