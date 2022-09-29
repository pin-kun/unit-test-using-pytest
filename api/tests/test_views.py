from unittest import TestCase
from urllib import response
import pytest
from classroom.models import Student, Classroom

# To create a student and fill up with random values, we are using mixer here
from mixer.backend.django import mixer

# Not to save the data that we generating to the database
# Prevents pytest to write the database
pytestmark = pytest.mark.django_db

# To call the url, we need something called "apiclient"
from django.test import TestCase
from rest_framework.test import APIClient

from rest_framework.reverse import reverse # to use the reverse "name" provided in urls.py


# while testing models, we create student object and test the models
# But in views.py, we are directly connected to urls.py
# So we call the urls.py and try to check whether we getting data or not

# Test class for student
class TestStudentListAPIVIews(TestCase):
    #setUp() function
    # To call the url, we need something called "apiclient"
    def setUp(self):
        self.myapiclient = APIClient() # "myapiclient" => can be given any variable name
        print('self.myapiclient-->: ', self.myapiclient)

    # get method
    def test_student_list_works(self):            
        # Create student data using mixer
        student = mixer.blend(Student, first_name="Krishna")
        student2 = mixer.blend(Student, first_name="balaram")

        # call the url
        # To call the url, we need something called "apiclient"
        # using the reverse "name" provided in urls.py. Even if we change the url, It won't affect test case
        url = reverse('student_list_api') 
        response = self.client.get(url) # "response" => can be given any variable name ('GET' method)
        print('response: ', response)
        print('dir_response: ', dir(response))

        # assertions
        # - json
        # - status
        assert response.json != None
        assert len(response.json()) == 2 # will fail because we created 2 students and checking the length == 1
        assert response.status_code == 200
        # assert False # Test case will Fail

    # post method
    def test_student_create_works(self): 
        # Generate data
        # "data_required" => can be given any variable name
        input_data = {
            "first_name": "arjun",
            "last_name": "kshatriya",
            "username": "",
            "admission_number": 3,
            "is_qualified": True,
            "average_score": 10
        }

        # call the url
        # To call the url, we need something called "apiclient"
        # using the reverse "name" provided in urls.py. So that even if we change the url, It won't affect test case
        url = reverse('student_create_api') 
        response = self.client.post(url, input_data) # "response" => can be given any variable name ('POST' method)

        # assertions
        # - json
        # - status
        print('post response -->', response.data)
        assert response.json != None
        assert response.status_code == 201
        assert Student.objects.count() == 3

    # retrieve ('GET') method
    def test_student_detail_works(self): 
        # Create student data using mixer
        student = mixer.blend(Student, first_name="naruto")
        student2 = mixer.blend(Student, first_name="goku")

        # call the url
        # To call the url, we need something called "apiclient"
        # using the reverse "name" provided in urls.py. So that even if we change the url, It won't affect test case
        url = reverse('student_detail_api', kwargs={"pk": 1})
        response = self.client.get(url) # "response" => can be given any variable name ('retrieve/get' method)

        # assertions
        # - json
        # - status
        print('detail response -->', response.data)
        assert response.json != None
        assert response.status_code == 200
        assert Student.objects.count() == 2

    # delete method
    def test_student_delete_works(self):
        """
            Here, first we will create 1 student, so count = 1 - will check using assert
            Then we will delete that crated 1 student, so count = 0 - will check using assert
        """

        # Create a student using mixer
        student = mixer.blend(Student, first_name="rahul")
        assert Student.objects.count() == 1 # if count=1 then student created

        # call the url
        # To call the url, we need something called "apiclient"
        # using the reverse "name" provided in urls.py. So that even if we change the url, It won't affect test case
        url = reverse('student_delete_api', kwargs={"pk": 1})
        response = self.client.delete(url) # "response" => can be given any variable name ('delete' method)

        # assertions
        # - json
        # - status
        print('delete response -->', response.data)
        print('status code for delete -->', response.status_code)
        assert response.status_code == 204
        assert Student.objects.count() == 0 # if count=0 then student deleted

# Test class for classroom using APIView
class TestClassroomAPIView(TestCase):
    #setUp() function
    # To call the url, we need something called "apiclient"
    def setUp(self):
        self.myapiclient = APIClient() # "myapiclient" => can be given any variable name
        print('self.myapiclient-->: ', self.myapiclient)

    def test_classroom_qs_works(self):
        classroom = mixer.blend(Classroom, student_capacity=20)
        classroom2 = mixer.blend(Classroom, student_capacity=28)

        # url reverse - using name from urls.py
        url = reverse("classroom_qs_api", kwargs={"student_capacity": 29})

        response = self.client.get(url)
        print('classroom data --> ', response.data)

        assert response.status_code == 202
        assert response.data["classroom_data"] != []
        assert response.data["number_of_classes"] == 2