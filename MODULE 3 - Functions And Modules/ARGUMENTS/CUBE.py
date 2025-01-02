def cubeofcubes (targetnumber):

    cube = (targetnumber**3)
    return cube

def divisibility (isitdivisibleby3):
    if (isitdivisibleby3%3 == 0):
        return cubeofcubes (isitdivisibleby3)
    
    else:
        return False

cube1 = int(input("ENTER USER INPUT: "))

print(f"THE CUBE OF {cube1} = {divisibility (cube1)}") 



