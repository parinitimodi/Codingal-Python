import array as arr
arraynum = arr.array("i",[1,3,5,3,7,9,3])
print("Original array: "+str(arraynum))
print("Number of occurences of the number 3 in the said array: "+str(arraynum.count(3)))
arraynum.reverse()
print("The reverse order of the items: ")
print(str(arraynum))