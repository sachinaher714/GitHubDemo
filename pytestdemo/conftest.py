import pytest


@pytest.fixture(scope="class") #execute fixeture before class and after executing all test cases
def setup():
    print(" execute first")
    yield
    print("execute last")


@pytest.fixture()
def dataload():
    return ["sachin","raman","aher"] #returns data at one time  #this send in test_demo2.py file


@pytest.fixture(params=[("chrome","browser"),("firefox","sachin"),("IE")])
def crossBrowser(request):  #request is tied up to request
    return request.param  #send multiple data but one by one at a time #this send in test_demo1.py file
