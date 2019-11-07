# Austin Daybell
# Guess my number Game
# 10/19

# imports
import random
import time

# functions


numplayers = input("How many people are playing? ")

if numplayers == "1":
    # functions
    def get_num_in_range(rmin,rmax):
        while True:
            guessinput = input("Pick a number between " +str(rmin) +" and "+str(rmax)+"\n")
            if guessinput.isdigit():
                guessinput = int(guessinput)
                if guessinput > rmin and guessinput < rmax:
                    return guessinput
            print("not a good value")

    def game(rmin,rmax,maxTrys):
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
    
    print("Welcome to the guess my number game")
    time.sleep(4)
    questioninp = input("""-----------------------------------------------------
What is the difficulty you are looking for with trys.
Easy = 15, medium = 10, hard = 5, and creative mode.
-----------------------------------------------------
""")
    questioninp = questioninp.upper()
    if questioninp == "EASY":
        maxTrys = 15
        rmin = 0
        rmax = 100
        game(rmin,rmax,maxTrys)
    if questioninp == "MEDIUM":
        maxTrys = 10
        rmin = 0
        rmax = 100
        game(rmin,rmax,maxTrys)
    if questioninp == "HARD":
        maxTrys = 5
        rmin = 0
        rmax = 100
        game(rmin,rmax,maxTrys)
    if questioninp == "CREATIVE":
        maxTrys = input("How many trys do you want them to have? ")
        rmin = input("What is the lowest random number do you want? ")
        rmax = input("What is the highest random number do you want? ")
        maxTrys = int(maxTrys)
        rmin = int(rmin)
        rmax = int(rmax)
        game(rmin,rmax,maxTrys)
else:
    # functions
    def get_num_in_range(rmin,rmax):
        while True:
            guessinput = input("Pick a number between " +str(rmin) +" and "+str(rmax)+"\n")
            if guessinput.isdigit():
                guessinput = int(guessinput)
                if guessinput > rmin and guessinput < rmax:
                    return guessinput
            print("not a good value")

    def game(rmin,rmax,maxTrys):
        word


        trys = 0

        
        
        guess = get_num_in_range(rmin,rmax)
        trys += 1 
        # starting game loop
        while guess != word and trys != maxTrys:
            if guess > word:
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
        if guess == word:
            print("Winner")
        else:
            print("Looser")
        print("Number was",word)

        
    print("Welcome to the guess my number game")
    time.sleep(4)
    print("----------------------------------------------------")
    maxTrys = input("How many trys do you want them to have? ")
    rmin = input("What is the lowest random number do you want? ")
    rmax = input("What is the highest random number do you want? ")
    word = input("Enter the number that you want them to guess. ")
    print("----------------------------------------------------")
    maxTrys = int(maxTrys)
    rmin = int(rmin)
    rmax = int(rmax)
    word = int(word)
    game(rmin,rmax,maxTrys)

    
    
        

        
    
        
