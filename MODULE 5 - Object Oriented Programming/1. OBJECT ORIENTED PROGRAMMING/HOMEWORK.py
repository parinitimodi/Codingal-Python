class Dog: 
    'A simple dog model.'

    def __init__(self, name, age): 
        'Construct name and age attributes for an instance of Dog'
        self.name = name.title()
        self.age = age

    def sit(self):
        'Simulate a dog sitting in response to a command.'
        print(self.name + " is now sitting.")

    def roll_over(self):
        'Simulate rolling over in response to a command.'
        print(self.name + " rolled over!")

my_dog = Dog(name='willie', age=6)

print("My dog's name is " + my_dog.name + ".")
print("My dog is " + str(my_dog.age) + " years old.")