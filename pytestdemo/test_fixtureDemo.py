import pytest


@pytest.mark.usefixtures("setup")
class Testmethod:

    def test_fixtureDemo(self):
        print("execute second")

    def test_fixtureDemo1(self):
        print("execute second")

    def test_fixtureDemo2(self):
        print("execute second")