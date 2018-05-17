import datetime
import random
import sys
import os

# a random number generator where the user inputs minimum values and max values
# allows the user to set ranges or to run mulitple generations at a datetime

selection = ""
while(True):

    print ("Welcome to the random number generator!")
    print ("1: run a single number generation")
    print ("2: run multiple generations")
    print ("3: create a commonly used generation")
    print ("4: exit program")
    selection = input(":")

    if selection == "1":
        min_val = ""
        max_val = ""
        print ("What do you want the minimum value to be?")
        min_val = input(">")
        print ("what do you want the maximum value to be?")
        max_val = input(">")
        print("your number is:")
        print ("--------------------")
        print(random.randint(int(min_val), int(max_val)))
        print ("--------------------")

    if selection == "2":
        times_run = ""
        min_val = ""
        max_val = ""
        print("how many numbers do you want to generate?")
        times_run = input(">")
        print ("What do you want the minimum value to be?")
        min_val = input(">")
        print ("what do you want the maximum value to be?")
        max_val = input(">")
        print("your numbers are:")
        print ("--------------------")
        for x in range(int(times_run)):
            print(random.randint(int(min_val), int(max_val)))
        print ("--------------------")

    if selection == "3":
        print ("-----------------------------")
        print("this program saves commonly used generations in text files")
        print("these files can be either created here, or added manually")
        print("the program will keep these files in a folder created at this location")
        print ("-----------------------------\n")
        print ("1: list all saved generations")
        print ("2: create a new saved generation")
        print ("3: run a saved generation")
        print ("4: return to main menu")
        selection = input(">")

        if selection == "1":
            cur_directory = pathlib.path("./saved generators")
            cur_pattern = "*.txt"
            for cur_file in cur_directory.glob(cur_pattern):
                print(cur_file)
        if selection == "2":
            pass
        if selection == "3":
            pass
        if selection == "4":
            pass




    if selection == "4":
        sys.exit()
