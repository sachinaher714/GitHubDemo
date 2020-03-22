import pytest


@pytest.mark.smoke     #to mark test cases for smoke or regression in future
def test_firstProgram():
    print("Hello")

#@pytest.mark.xfail
def test_hobby():
    print("cricket")

#@pytest.mark.usefixtures("crossBrowser")


def test_crossBrowser(crossBrowser):  #self is not required as method is not wrappeed under class
    print(crossBrowser)


