# unit-test-using-pytest
Here I used pytest for unit testing.

##### What am I testing here?
  - Models
  - DRF (Django Rest Framework) / API Tetsing
  - Views
  
  
##### What am I using for testing?
  - I have tested using Django Model Tests `TestCase`
  - Tested using `Pytest`
  - Using `hypothesis` library with `pytest` which gives us lots of benefits and easeness while testing
 
 
 ##### What am I using for testing?
  - I have tested using Django Model Tests `TestCase`
  - Using `Pytest` for Python test
  - Using `mixer` library for random values
    - **mixer**:
      - It will create a student model for us
      - It will fill up the variables with random_values in the models for us
      - We can also give 'static value' to the model variables 
  - Using `hypothesis` library with `pytest` which gives us lots of benefits and easeness while testing
    - **hypothesis**:
      - With the use of `mixer` and `hypothesis`, we can check different scinarios that we would not have thought of before.
      - We can use @given() decorator to fill up the model variables with random_values (using `mixer.blend()`)



#
 
 
 ##### How to run and test this project?
1. Clone the repo into your local system: `git clone https://github.com/pin-kun/unit-test-using-pytest.git`
2. Create your own **virtual environment (venv)** and **actvate** it. Linux command: `source your_venv/bin/activate`
3. Now in that virutal env, install the libraries and packages that I have used in this project
    - Run this command to install all the libraries in vnenv: `pip install -r requirements.txt`
4. Go to the project base directory and run this project
    - Command to run this project locally: `python manage.py runserver`
    - Django Admin Panel credentials: 
        - url: http://127.0.0.1:8000/admin/
        - username: **admin**
        - password: **admin**
    
