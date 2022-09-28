from django.test import TestCase
import pytest
from .models import Classroom, Student
from hypothesis import strategies as st, given


# import mixer for generating random values
from mixer.backend.django import mixer

# Not to save the data that we generating to the database
# Prevents pytest to write the database
pytestmark = pytest.mark.django_db

# We are going to use mixer() which will generate random numbers
class TestStudentModel:
    # We have to start every function with "test_" name

    # simple calculation test case
    def test_a_plus_b(self):
        a = 1
        b = 2
        c = a + b
        assert c == 3

    # Confirm student data
    def test_student_can_be_created(self):
        
        # Creating a mixer vaiable and applying on "Student" model 
        # Overwriting the "first_name" with "Tom"
        student1 = mixer.blend(Student, first_name="Tom")
        student_result = Student.objects.last() # getting the last student
        assert student_result.first_name == "Tom"
    
    # Check the dunder function (__str__)
    def test_str_return(self):
        student1 = mixer.blend(Student, first_name="Tom")
        student_result = Student.objects.last() # getting the last student
        assert str(student_result) == "Tom"

    # check username - slug field
    # @given(st.characters())
    # def test_slugify(self, slug_name):
    #     student1 = mixer.blend(Student, username=slug_name)
    #     student_result = Student.objects.last() # getting the last student
    #     assert len(student_result.username) == len(slug_name)

    # Check the get_grade() function -  for FAIL case
    @given(st.floats(min_value=0, max_value=40)) # will return a value
    def test_get_grade_fail(self, fail_score): # "fail_score" will get a value from "@given"
        print('fail_score---', fail_score)
        student1 = mixer.blend(Student, average_score=fail_score)
        student_result = Student.objects.last() # getting the last student
        assert student_result.get_grade() == "Fail"

    # Check the get_grade() function - for PASS case   
    @given(st.floats(min_value=41, max_value=70)) # will return a value
    def test_get_grade_pass(self, pass_score): # "pass_score" will get a value from "@given"
        
        student1 = mixer.blend(Student, average_score=pass_score)
        student_result = Student.objects.last() # getting the last student
        assert student_result.get_grade() == "Pass"

    # Check the get_grade() function - for EXCELLENT case
    @given(st.floats(min_value=71, max_value=100)) # will return a value
    def test_get_grade_excellent(self, excellent_score): # "excellent_score" will get a value from "@given"
        
        student1 = mixer.blend(Student, average_score=excellent_score)
        student_result = Student.objects.last() # getting the last student
        assert student_result.get_grade() == "Excellent"

    # Check the get_grade() function - for Error case
    @given(st.floats(min_value=101)) # will return a value
    def test_get_grade_error(self, error_score): # "error_score" will get a value from "@given"):
        
        student1 = mixer.blend(Student, average_score=error_score)
        student_result = Student.objects.last() # getting the last student
        assert student_result.get_grade() == "Error"

class TestClassroomModel:
    def test_classroom_create(self):
        classroom = mixer.blend(Classroom, name="Tom")
        classroom_result = Classroom.objects.last() # getting the last student
        assert str(classroom_result) == "Tom"

        