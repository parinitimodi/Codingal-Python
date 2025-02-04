user_input = int(input("Enter a number: "))


odd_numbers_under = [i for i in range(user_input) if i % 2 != 0]

odd_numbers = [i for i in range(1, user_input + 1) if i % 2 != 0]

print("Odd numbers under", user_input, ":", odd_numbers_under)

print("List of odd numbers from 1 to", user_input, ":", odd_numbers)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Capitalized fruits:", capitalized_fruits)
print("THANKS!!")