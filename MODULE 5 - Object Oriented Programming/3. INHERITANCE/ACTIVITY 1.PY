class Birds:
    def __init__(self):
        print("Bird is Ready!!")
    def whoisthis(self):
        print("Bird !!")
    def swim(self):
        print("Swim Faster!!")
class Penguin (Birds):
    def __init__(self):
        super().__init__()
        print("Penguin is ready!!")
    def whoisthis (self):
        print("Penguin!!")
    def run (self):
        print("Run Faster!!")

peggy = Penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()