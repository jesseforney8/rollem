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
        return total


total_list = []


def ask():
    side = int(input("How many sides? "))
    amt = int(input("How many dice? "))
    total_list.append(Dice(side, amt).roll())
    print(total_list)


def say_total(lst):
    total1 = sum(lst)
    print("This is the total of all dice:", total1)


def another_dice():
    new_yes_no = str(input("Do you want another type of dice? y/n ")).lower()
    if new_yes_no == "y":
        ask()
    elif new_yes_no == "n":
        say_total(total_list)
    else:
        pass


is_running = True

while is_running:
    ask()
    another_dice()

