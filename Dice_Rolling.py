# Dice Rolling game.  I frequently play board games with my wife and kids.
# Kids are kids and the dice tend to go missing... CAN'T LOSE DICE IN PYTHON!
# I still haven't figured out why it says "none" at the end of the while loop.
# If I use this in a supported application each of these functions will be brought into their own code and nested in a
# drop down menu

import random

# Dice Roll sets
def dice_roll(dice_num):
    sides = int(input("How many sides do you want on your dice? "))
    min = 1
    max = sides
    roll_again = 0
    while roll_again < dice_num:
        print("You rolled a....")
        print(random.randint(min, max))
        roll_again += 1

#For Memoir 1944
def memoir_dice_roll(dice_num):
    memoir_dice = ["Infantry", "Infantry", "Calvary", "Calvary", "Artillery", "Flag"]
    roll_again = 0
    while roll_again < dice_num:
        print("You rolled a....")
        print(random.choice(memoir_dice))
        roll_again += 1

#For Fallout Board Game
def VATs_Dice_Roll(dice_num):
    memoir_dice = ["Head", "Arms 1 VAT", "Arms", "Chest 2 VAT", "Chest 1 VAT", "Chest "]
    roll_again = 0
    while roll_again < dice_num:
        print("You rolled a....")
        print(random.choice(memoir_dice))
        roll_again += 1

# Dice Roll - comment out the roll you don't need.
dice_num = int(input("How many dice are you rolling? "))

#print(dice_roll(dice_num))

#print(memoir_dice_roll(dice_num))

print(VATs_Dice_Roll(dice_num))