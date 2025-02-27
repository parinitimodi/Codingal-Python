class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
            return self.word + "(" + self.meaning + ")"
flash = []
print("Welcome to flashcard application!")
while(True):
    word = input("Enter the name of the word you want to put in the flashcard...")
    meaning = input("Enter the meaning of the word you have entered in your flashcard...")
    flash.append(flashcard(word,meaning))
    option = int(input("Enter 0 if you want to add another flashcard, otherwise Enter 1 if you wish to stop..."))
    if (option):
        break
print("Your flashcards")
for i in flash:
    print(">", i )