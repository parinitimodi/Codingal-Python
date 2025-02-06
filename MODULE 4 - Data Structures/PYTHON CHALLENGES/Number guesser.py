import random
import time
number =random.randint(1,100)
def intro():
    print("May i ask your name?")
    global name
    name = input()
    print(name + ",we are going to play a game. Guess a number from 1 to 100")
    if (number%2 == 0):
        x = "even"
    else:
        x = "odd"
    print(f"\n This is an {x} number")
    time.sleep(.5)
    print("Go ahead. Guess!!")
def pick():
    guesstaken = 0
    while guesstaken<6:
        time.sleep(.25)
        enter = input("Guess: ")
        try:
            guess = int(enter)
            if (guess<=100 and guess>=1):
                guesstaken = guesstaken + 1
                if guesstaken<6:
                    if guess<number:
                        print ("The guess of the number you have guessed is lower")
                    if guess>number:
                        print ("The guess of the number you have guessed is higher")
                    if guess!=number:
                        time.sleep(.5)
                        print("TRY AGAIN!!")
                    if guess == number:
                        break
            if guess>100 or guess<1:
                print("SILLY GOOSE! That number is not in the range!!")
                time.sleep(.25)
                print("Please enter a number between 1 and 100")
        except:
                print("I dont think that "+enter+"is a number. SORRY!")
    if guess == number:
        guesstaken = str(guesstaken)
        print(f"Good Job,{name}!You guessed it in {guesstaken}")
    if guess != number:
        print("NOPE. The number i was thinking of was"+str(number))
play = "yes"
while(play == "yes" or play == "y"):
    intro()
    pick()
    print("Do u want to play again?")
    play = input("Enter yes or no")







