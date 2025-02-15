print("I have 2 dogs, Murphy and Cocoa.")
class Dogs:
    species = "Golden Retriever"
    otherspecies = "Shih Tzu"
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
Murphy = Dogs ("Murphy",9,"Male")
Cocoa = Dogs ("Cocoa",8,"Female")
print("Murphy is a {}".format(Murphy.species))
print("He is {} years old".format(Murphy.age))
print(" Murphy is a",(Murphy.gender))
print("Cocoa is a {}".format(Cocoa.otherspecies))
print("She is {} years old".format(Cocoa.age))
print("Cocoa is a",(Cocoa.gender))
