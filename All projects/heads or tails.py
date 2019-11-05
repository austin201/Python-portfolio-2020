# Austin Daybell
# Head or Tails

heads_or_tails = input("What do you think will happen the most? heads or tails? ")
user_range = input("How many times do you want it to flip heads or tails? ")

import random

def heads():
    print(
    """
     _    _                      _       
    | |  | |                    | |      
    | |__| |   ___    __ _    __| |  ___ 
    |  __  |  / _ \  / _` |  / _` | / __|
    | |  | | |  __/ | (_| | | (_| | \\__ \\
    |_|  |_|  \___|  \__,_|  \__,_| |___/

                                        """)

def tails():
    print(
    """
      _______           _   _       
     |__   __|         (_) | |      
        | |      __ _   _  | |  ___ 
        | |     / _` | | | | | / __|
        | |    | (_| | | | | | \\__ \\
        |_|     \__,_| |_| |_| |___/

                                    """)

print("You chose",heads_or_tails)
for i in range(int(user_range)):
    num = random.randint(0,1)+1
    if num == 1:
        heads()
    else:
        tails()
   



