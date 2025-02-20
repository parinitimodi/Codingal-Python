class myClass:
    __privateVar = 27
    def __privMeth(self):
        print("Im inside class myClass")
    def hello(self):
        print("private Variable Value: ",myClass. __privateVar)
foo = myClass()
foo.hello()
foo.__privMeth()