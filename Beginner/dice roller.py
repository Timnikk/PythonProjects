##Make the a program that can roll the dice. The user can choose how many dices to roll.
import random
dice = [1, 2, 3, 4, 5 , 6]
x = int(input("How many dices do you want to roll at one time?: "))
n = 1
for n in range (1,x+1):
    print("The " + str(n) + " dice rolled: " + str(random.choice(dice)))
    n += 1
