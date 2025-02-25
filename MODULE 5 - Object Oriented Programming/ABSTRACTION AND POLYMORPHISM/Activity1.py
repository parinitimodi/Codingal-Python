from abc import ABC,abstractmethod
class Absclass (ABC):
    def print(self,x):
        print("Passed Value:",x)
    @abstractmethod
    def task (self):
        print("We are inside Absclass task")
class testclass(Absclass):
    def task (self):
        print("We are inside testclass task")
testobj = testclass()
testobj.task()
testobj.print(100)