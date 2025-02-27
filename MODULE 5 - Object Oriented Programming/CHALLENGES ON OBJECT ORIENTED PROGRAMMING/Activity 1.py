class A:
    def __init__ (self,a):
        self.a = a
    def __lt__(self,other):
            if (self.a<other.a):
                    return("OB1<OB2")
            else:
                   return ("OB1>OB2")
    def __eq__(self,other):
        if (self.a == other.a):
                  print ("Both are equal")
        else:
               print("Neither of then are equal")
ob1 = A(2)
ob2 = A(3)
print("Passed values:",ob1.a,ob2.a)
ob3 = A(4)
ob4 = A(4)
print("Passed values:",ob3.a,ob4.a)
print("OB3 == OB4")     