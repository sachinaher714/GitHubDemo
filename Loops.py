class sachin:
    age=100
    a=0
    b=0
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
        print("new")

    def getname(self):
        print("one")

    def sum(self):
        return self.num1+self.num2



obj =sachin(2, 3)
obj.getname()
print(obj.sum())


