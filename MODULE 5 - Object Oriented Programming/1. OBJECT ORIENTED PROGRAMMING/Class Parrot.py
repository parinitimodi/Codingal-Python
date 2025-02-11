class Friends:
    species = "Human"
    def __init__(self,name,age):
        self.name = name
        self.age = age
Vihani = Friends ("Vihani",12)
Vihaan = Friends ("Vihaan",12)
Pariniti = Friends ("Pariniti",11)
Vamshi = Friends ("Vamshi",11)
print("Vihani is a {}".format(Vihani.species))
print("Vihaan is a {}".format(Vihaan.species))
print("Pariniti is a {}".format(Pariniti.species))
print("Vamshi is a {}".format(Vamshi.species))
print("{} is {} years old".format(Vamshi.name,Vamshi.age))