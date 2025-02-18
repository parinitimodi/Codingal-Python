class Vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class Bus(Vehicle):
    pass
schoolbus = Bus("School Volvo",18,12)
print("Vehicle name:",schoolbus.name,"Speed:",schoolbus.maxspeed,"Mileage:",schoolbus.mileage,".")