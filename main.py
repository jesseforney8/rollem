import random


class Dice:
    roll_number = 0
    num_list = []
    counter = 0

    def __init__(self, num_side, amount):
        self.num_side = num_side
        self.amount = amount

    def roll(self):
        print("These are the rolls for the dice with ", self.num_side, "sides: ")
        while self.amount > 0:
            self.roll_number = random.randrange(1, self.num_side + 1)
            self.num_list.append(self.roll_number)
            print(self.counter + 1, ": ", self.num_list[self.counter])
            self.amount -= 1
            self.counter += 1
        total = sum(self.num_list)
        print("this is the total: ", total)


is_running = True

while is_running:
    side = int(input("How many sides? "))
    amt = int(input("How many dice? "))
    dice1 = Dice(side, amt)
    dice1.roll()
    yes_no = True
    while yes_no:
        leave = str(input("Exit? y/n ")).lower()
        if leave == "y":
            is_running = False
            break
        elif leave == "n":
            yes_no = False
            break
        else:
            print("invalid!!!!")

