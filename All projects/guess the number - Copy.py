# Austin Daybell
# Guess my number Game
# 10/19

# imports
import random
import time

# functions
def get_num_in_range(rmin,rmax):
    while True:
        guessinput = input("Pick a number between " +str(rmin) +" and "+str(rmax)+"\n")
        if guessinput.isdigit():
            guessinput = int(guessinput)
            if guessinput > rmin and guessinput < rmax:
                return guessinput
        print("not a good value")


def intro():
    print("""What difficulty are you looking for easy, medium, hard, or custimize.
Computer play is not working at this time do not pick that option.
If you want to quit enter number 6.

    1. easy
    2. medium
    3. hard
    4. custimize
    5. computer
    6. quit
""")
def difeasy():
    global maxTrys
    global rmin
    global rmax
    maxTrys = 15
    rmin = 0
    rmax = 100
    
    game(rmin,rmax,maxTrys)

   

def difmedium():
    global maxTrys
    global rmin
    global rmax
    maxTrys = 10
    rmin = 0
    rmax = 100
    game(rmin,rmax,maxTrys)

    

def difhard():
    global maxTrys
    global rmin
    global rmax
    maxTrys = 5
    rmin = 0
    rmax = 100
    game(rmin,rmax,maxTrys)

def custimization():
    global maxTrys
    global rmin
    global rmax

    maxTrys = int(input("""What do you want your max trys to be?
"""))
    rmin = int(input("""What is the minimum you want to have?
"""))
    rmax = int(input("""What is the maximum you want to have?
"""))
    game(rmin,rmax,maxTrys)

def gamecomp():
    rmin = 0
    rmax = 100
    maxTrys =5
    randnum = random.randint(rmin,rmax)
    gmin = 1
    gmax =100
    x = randnum = random.randint(gmin,gmax)
    if x == randnum:
        print("The computer won")
        option()
    else:
        print("You won")
    if x > randnum:
        gmin = 50
        return x
    if x < randnum:
        gmax = 50
        return x

def leave():
    confirmation = input("""Are you sure you want to exit the program.(yes or no)
""")
    confirmation = confirmation.lower()
    if confirmation == "yes":
        quit()
    if confirmation == "no":
        option()

def option():
    while True:
        intro()
        choice = input("""Pick an option 1,2,3,4,5, or 6
""")
        if choice == "1":
            difeasy()
        if choice == "2":
            difmedium()
        if choice == "3":
            difhard()
        if choice == "4":
            custimization()
        if choice == "5":
            leave()
        if choice == "6":
            leave()

def game(rmin,rmax,maxTrys):
    print("Welcome to the guess my number game")
    time.sleep(4)
    randnum = random.randint(rmin,rmax)


    trys = 0

    
    
    guess = get_num_in_range(rmin,rmax)
    trys += 1 
    # starting game loop
    while guess != randnum and trys != maxTrys:
        if guess > randnum:
            totaltrys = maxTrys - trys
            print("---------------------------------------------")
            print("Guess Lower")
            print("Max trys:",maxTrys)
            print("Trys:",trys)
            print("Trys left:",totaltrys)
            print("---------------------------------------------")
        else:
            totaltrys = maxTrys - trys
            print("---------------------------------------------")
            print("Guess Higher")
            print("Max trys:",maxTrys)
            print("Trys:",trys)
            print("Trys left:",totaltrys)
            print("---------------------------------------------")
        guess = get_num_in_range(rmin,rmax)
        trys += 1

    # ending game loop
    if guess == randnum:
        print("Winner")
    else:
        print("Looser")
    print("Number was",randnum)


# set up program vars
maxTrys = 10
option()



            
        
