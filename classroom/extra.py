from django.test import TestCase
from .models import Student

# Before using setUp() function - Redundant code
# class TestStudentModel(TestCase):
#     # We have to start every function with "test_" name
#     # simple calculation test case
#     def test_a_plus_b(self):
#         a = 1
#         b = 2
#         c = a + b
#         self.assertEqual(c, 3)

#     # Confirm student data
#     def test_student_can_be_created(self):
#         student1 = Student.objects.create(
#             first_name = "Tom",
#             last_name = "Holand",
#             admission_number = 1
#         )
#         student_result = Student.objects.last() # getting a last student
#         self.assertEqual(student_result.first_name, "Tom")
    
#     # Check the dunder function (__str__)
#     def test_str_return(self):
#         student1 = Student.objects.create(
#             first_name = "Tom",
#             last_name = "Holand",
#             admission_number = 1
#         )
#         student_result = Student.objects.last() # getting a last student
#         # print(str(student_result))
#         self.assertEqual(str(student_result), "Tom")

#     # Check the get_grade() function -  for FAIL case   
#     def test_get_grade_fail(self):
#         student1 = Student.objects.create(
#             first_name = "Tom",
#             last_name = "Holand",
#             admission_number = 1,
#             average_score = 39
#         )
#         student_result = Student.objects.last()
#         self.assertEqual(student_result.get_grade(), "Fail")

#     # Check the get_grade() function -  for PASS case   
#     def test_get_grade_fail(self):
#         student1 = Student.objects.create(
#             first_name = "Tom",
#             last_name = "Holand",
#             admission_number = 1,
#             average_score = 65
#         )
#         student_result = Student.objects.last()
#         self.assertEqual(student_result.get_grade(), "Pass")

#     # Check the get_grade() function -  for EXCELLENT case   
#     def test_get_grade_fail(self):
#         student1 = Student.objects.create(
#             first_name = "Tom",
#             last_name = "Holand",
#             admission_number = 1,
#             average_score = 81
#         )
#         student_result = Student.objects.last()
#         self.assertEqual(student_result.get_grade(), "Excellent")

        