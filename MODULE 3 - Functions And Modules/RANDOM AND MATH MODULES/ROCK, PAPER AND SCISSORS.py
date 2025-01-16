import random
value = str(input("Enter either Rock, Paper or Scissors "))
compvalue = ["Rock","Paper","Scissors"]

compvaluefinal = (random.choice(compvalue))
print("The answer entered by the computer is ",compvaluefinal)

if (compvaluefinal == value):
    print("Its a draw!!")
elif (compvaluefinal == "Rock" and value == "Scissors"):
    print("The computer wins!!")
elif (compvaluefinal == "Scissors" and value == "Paper"):
    print("The computer wins!!")
elif (compvaluefinal == "Paper" and value == "Rock"):
    print("The computer wins!!")
else:
    print("You win!!")