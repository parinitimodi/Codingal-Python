
# create an empty dictionary

lookup = {}

# Iterate through the tuple

for i, num in enumerate(nums):

    if target - num in lookup:

        return (lookup[target - num], i )

lookup[num] = i

# take input of dum from the user

value = int(input("Enter sum for which you want to make this search : "))

print(pair_elements().twoSum((10,20,30,40,50,60,70),value))


    