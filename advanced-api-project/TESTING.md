Testing Framework
The testing framework used for this project is Django's built-in testing framework, which is based on Python's unittest module.

Types of Tests
The following types of tests are performed:

- Unit tests: Test individual components of the API, such as models, views, and serializers.
- Integration tests: Test how different components of the API interact with each other.
- API endpoint tests: Test the API endpoints to ensure they return the correct data and status codes.

Running the Tests
To run the tests, navigate to the project directory and run the following command:


bash
python3 manage.py test api


Interpreting Test Results
The test results will indicate whether each test passed or failed. If a test fails, the output will include an error message indicating why the test failed.
