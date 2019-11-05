# Austin Daybell
# Guess my number Game
# 10/19

# imports
import random

print("Make sure to not play in full screen")
players = input("""How many Players are playing
""")
if players == "1":
    def get_num_in_range(rmin,rmax):
        while True:
            guessinput = input("Pick a number between " +str(rmin) +" and "+str(rmax)+"\n")
            if guessinput.isdigit():
                guessinput = int(guessinput)
                if guessinput > rmin and guessinput < rmax:
                    return guessinput
            print("not a good value")

    maxTrys = input("""What difficult do you want?(easy, medium, hard, or creative)
""")
    if maxTrys == "easy":
        maxTrys = 20
        rmin = 0
        rmax = 100
        randnum = random.randint(rmin,rmax)
    if maxTrys == "medium":
        maxTrys = 15
        rmin = 0
        rmax = 100
        randnum = random.randint(rmin,rmax)
    if maxTrys == "hard":
        maxTrys = 10
        rmin = 0
        rmax = 100
        randnum = random.randint(rmin,rmax)
    if maxTrys == "creative":
        rmin = input("""What do you want the minimum to be
    """)
        rmax = input("""What do you want the maximum to be
    """)
        maxTrys = input("""How many trys do you want to have
    """)
        rmin = int(rmin)
        rmax = int(rmax)
        randnum = random.randint(rmin,rmax)
        maxTrys = int(maxTrys)
        
    trys = 0    
    guess = get_num_in_range(rmin,rmax)
    trys += 1
    while guess != randnum and trys != maxTrys:
        if guess > randnum:
            print("Guess Lower")
        else:
            print("Guess Higher")
        guess = get_num_in_range(rmin,rmax)
        trys += 1
    if guess == randnum:
        print("Winner")
    else:
        print("Looser")
    print("Number was",randnum)
    
else:
    print("Make everyone but the picker leave the room.")
    rmin = input("""What do you want the minimum to be
""")
    rmax = input("""What do you want the maximum to be
""")
    maxTrys = input("""How many trys do you want them to have
""")
    maxTrys = int(maxTrys)
    
    num1 = input("What number do you want them to guess? ")
    num1 = int(num1)

    space = input("""














































Just press enter? """)

    
    def get_num_in_range(rmin,rmax):
        while True:
            guessinput = input("Pick a number between " +str(rmin) +" and "+str(rmax)+"\n")
            if guessinput.isdigit():
                guessinput = int(guessinput)
                if guessinput > int(rmin) and guessinput < int(rmax):
                    return guessinput
            print("not a good value")
        
    trys = 0    
    guess = get_num_in_range(rmin,rmax)
    trys += 1
    while guess != num1 and trys != maxTrys:
        if guess > num1:
            print("Guess Lower")
        else:
            print("Guess Higher")
        guess = get_num_in_range(rmin,rmax)
        trys += 1
    if guess == num1:
        print("Winner")
    else:
        print("Looser")
    print("Number was",num1)

            
        
