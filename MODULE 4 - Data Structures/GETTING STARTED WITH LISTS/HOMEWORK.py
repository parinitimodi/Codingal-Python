a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [n for n in a if n % 2 == 0]
odds = [n for n in a if n % 2 != 0]

print(a)
print("Even numbers from the list are",evens)  
print("Odd numbers from the list are",odds)

res = [i * i for i in a if i % 2 != 0]
print("Square of the elements =", res)