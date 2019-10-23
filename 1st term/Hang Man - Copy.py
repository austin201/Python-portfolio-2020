import random

WORD_BANK = ()
HANGMAN = (
"""
 ______
 |    |
 |    
 |
 |
 |
 |
 |
 |
-----------
""",
"""
 ______
 |    |
 |    o
 |
 |
 |
 |
 |
 |
-----------
""",
"""
 ______
 |    |
 |    o
 |    +
 |    | 
 |
 |
 |
 |
-----------
""",
"""
 ______
 |    |
 |    o
 |    +
 |    | 
 |   / \\
 |
 |
 |
-----------
""",
"""
 ______
 |    |
 |    o
 |   -+-
 |    | 
 |   / \\
 |
 |
 |
-----------
""",
"""
 ______
 |    |
 |    o
 |  /-+-\\
 |    | 
 |   / \\
 |   | |
 |
 |
-----------
""",
"""
 ______
 |    |
 |    o
 |  /-+-\\
 |    | 
 |   / \\
 |   | |
 |  -   -
 |
-----------
""")

num_players = int(input("How many players are playing? "))
if num_players == 1:

    MAX_WRONG = len(HANGMAN) -1
    WORD_BANK =["OVERUSED", "CLAM", "DICTIONARY", "TAFFETA", "PYTHON", "SLAM",\
                "SHADOW", "PEPPER", "MOOSE", "COCO", "TITANS", "STEELERS",\
                "DOLPHINS", "HOUSE", "CAR", "TRUCK", "BROTHER", "SISTER", "MOM",\
                "DAD", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY",\
                "SATURDAY", "SUNDAY", "TODAY", "TOMORROW", "FOOTBALL", "UTAH",\
                "WASHINGTON", "BOO", "ZOO", "WHO", "PHONE", "GOOGLE", "JAZZ",\
                "CHIPS", "CRACKERS", "PEN", "PENCIL", "CALCULATOR", "HELLO",\
                "GIB", "CODING", "CODE", "AUNTIE", "KYLEE", "KYLER", "KAYDEN",\
                "KENZIE", "SOCCER", "BASKETBALL", "KENT", "KAYLENE", "XBOX",\
                "TOUCHDOWN", "CARD", "CAKE", "CALIFORNIA", "YELLOWSTONE",\
                "PUPPIES", "DOG", "CHICKEN", "MINECRAFT", "FORTNITE", "DOOM",\
                "FALLOUT76", "COMPUTER", "PACK", "ICE", "SCHOOL", "WORLD",\
                "CRUEL", "COW", "PIG", "TURTLE", "FISH", "TURKEY", "CHRISTMAS",\
                "THANKSGIVING", "HALLOWEEN", "MOUSE", "MICE", "KEYBOARD",\
                "PRESENTING", "GAMES", "ARK", "SURVIVAL", "WINDOW", "DOOR",\
                "DESTINY", "SCISSORS", "GOOGLE", "MEET", "MEME", "STUDIO",\
                "HAMBURGER"]

    word = random.choice(WORD_BANK) # the word to be guessed
    so_far = "-" * len(word) # one dash for each letter in word to be guessed

    wrong = 0 # number of wrong guesses player has made
    used = [] # letters already guessed

    
    print("Welcome to Hangman. Good luck!")

    while wrong <MAX_WRONG and so_far != word:
        
        print(HANGMAN[wrong])
        print("\nYou've used the following letters:\n", used)
        print("\nSo far, the word is:\n", so_far)

        guess = input("\n\nEnter your guess: ")
        guess = guess.upper()

        while guess in used:
            print("You've already guessed the letter", guess)
            guess = input("\n\nEnter your guess: ")
            guess = guess.upper()

        used.append(guess)
        if guess in word:
            print("\nYes!", guess, "is in the word!")
            new = ""

            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new
        else:
            print("\nSorry,", guess, "isn't in the word.")
            wrong += 1

    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("\nYou've been hanged!")
    else:
        print("\nYou guessed it!")

    print("\n The word was", word)
    input("\n\nPress the Enter key to exit")

else:
    print("Have everyone but one person leave the room and have that person chooses a word")

    MAX_WRONG = len(HANGMAN) -1
    WORD_BANK = input("""What is your choosen word? """)
    WORD_BANK = WORD_BANK.upper()
    name = input("""







































What is your name? """)

    
    
    word = (WORD_BANK) # the word to be guessed
    so_far = "-" * len(word) # one dash for each letter in word to be guessed

    wrong = 0 # number of wrong guesses player has made
    used = [] # letters already guessed

    
    print("""Welcome to Hangman. Good luck!""")

    while wrong <MAX_WRONG and so_far != word:
        
        print(HANGMAN[wrong])
        print("\nYou've used the following letters:\n", used)
        print("\nSo far, the word is:\n", so_far)

        guess = input("\n\nEnter your guess: ")
        guess = guess.upper()

        while guess in used:
            print("You've already guessed the letter", guess)
            guess = input("\n\nEnter your guess: ")
            guess = guess.upper()

        used.append(guess)
        if guess in word:
            print("\nYes!", guess, "is in the word!")
            new = ""

            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new
        else:
            print("\nSorry,", guess, "isn't in the word.")
            wrong += 1

    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("\nYou've been hanged!")
    else:
        print("\nYou guessed it!")

    print("\n The word was", word)
    input("\n\nPress the Enter key to exit")






        
        

    








    
