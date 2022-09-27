from unittest import TestCase
from urllib import response
import pytest
from classroom.models import Student

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
class TestStudentListAPIVIews(TestCase):
    #setUp() function
    def setUp(self):
        self.myapiclient = APIClient() # "myapiclient" => you can give any name
        print('self.myapiclient: ', self.myapiclient)

    def test_student_list_works(self):            
        # create a student
        student = mixer.blend(Student, first_name="Krishna")
        student2 = mixer.blend(Student, first_name="balaram")

        # call the url
        # To call the url, we need something called "apiclient"
        # using the reverse "name" provided in urls.py. Even if we change the url, It won't affect test case
        url = reverse('student_list_api') 
        response = self.client.get(url) # "response" => you can give any name
        print('response: ', response)
        print('dir_response: ', dir(response))

        # assertions
        # - json
        # - status
        assert response.json != None
        assert len(response.json()) == 1 # will fail because we created 2 students and checking the length == 1
        assert response.status_code == 200
        # assert False # Test case will Fail
