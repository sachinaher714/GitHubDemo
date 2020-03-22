import pytest

from pytestdemo.BaseClass import BaseClass


def testfirstProgram():
    var="sachin"
    assert var=="sachin", "not match"

#@pytest.mark.smoke
#@pytest.mark.skip
def test_hobby():
    print("dance")

@pytest.mark.usefixtures("dataload")
#class Testexam2:  #if you wrapped the method under class then you dont need to use class
class TestExample(BaseClass):

    def testdata(self,dataload):
        print(dataload)
        #log=self.getlogger()
        #log.info(dataload[0])
        #print(dataload[1])
