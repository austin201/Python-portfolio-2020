 
def intro():
    print("""What type of dog breed is your favorite?
Choose from the list below by usin the number.

        1. German Shepherd
        2. Shih Tzu
        3. Golden Retriever
        4. Bulldog
        5. Websites
        6. quit
""")

def Shepherd():
    print("""
------------------------------------------------
The dog you chose is a German Shepherd.
This is info on the German Shepherd.

Size: Medium-Large working dog.

Life Expectancy: 9-13 years.

Weight
Male: 66-88 pounds(30-40kg)
Female: 49-71 pounds(22-32kg)

Colors: Black, Black & Tan, Red & Black,
Grey, Black & Silver.

Temperament: Intelligent, Loyal, Obedient,
Curious, Alert, Confident, Watchful, Courageous. 

Height
Male: 24-26 inches(60-65cm)
Female: 22-24 inches(55-60cm)

Cost:
Adult Fee: $375
Puppies under 6 months: $325
Puppies 7 months and up: $150
Yearly cost: $1,200-$1,500
___________________
|                 |
|                 |
|        |`-._ _  |
|        / `  _/  |
|        ****`    |
|       /    }    |
|      /  \ /     |
|  \ /`   \\\\\\     |
|   `\    /_\\\\    |
|    `~~~~~``~`   |
-------------------
------------------------------------------------
""")

def Shihtzu():
    print("""
---------------------------------------------------
The dog you chose is Shih Tzu.
This is info about a Shih Tzu. Has shorter info.

weight: 4-7.25kg when fully grown.

Hypoallergenic: Yes

Life Expectancy: 10-16 years

Temperament: Clever, Intelligent, Affectionate,
Lively, Active, Loyal, Spunky, Independent, Alert.

Colors: Black, White, Black and White, Light Brown,
Dark Brown, Blue, Gold.

Cost: $500-$1000 on average.
___________________
|                 |
|                 |
|        |`-._ _  |
|        / `  _/  |
|        ****`    |
|       /    }    |
|      /  \ /     |
|  \ /`   \\\\\\     |
|   `\    /_\\\\    |
|    `~~~~~``~`   |
-------------------
---------------------------------------------------
""")

def Gold():
    print("""
------------------------------------------------------
The dog you chose is Golden Retriever.
This is info about a Golden Retriever.

Size: Large gun dog

Life Expectancy: 10-12 years.

Weight:
Male: 65-75 pounds(30-34kg)
Female: 55-71 pounds(25-32kg)

Colors: Cream, Dark Golden, Light Golden, Golden.

Temperament: Reliable, Intelligent, Kind, Trustworthy,
Confident, Friendly.

Height:
Male: 22-24 inches(56-61cm)
Female: 20-22 inches(51-56cm)

Cost: $500-$3,000 depends on quality.
___________________
|                 |
|                 |
|        |`-._ _  |
|        / `  _/  |
|        ****`    |
|       /    }    |
|      /  \ /     |
|  \ /`   \\\\\\     |
|   `\    /_\\\\    |
|    `~~~~~``~`   |
-------------------
-----------------------------------------------------
""")

def Bull():
    print("""
----------------------------------------------------
The dog you chose is Bulldog.
This is info about a Bulldog.

Size: Medium

Life Expectancy: 8-10 years.

Weight:
Male: 51-55 pounds(23-25kg)
Female: 40-51 pounds(18-23kg)

Colors: White, Red & White, Red.

Temperament: Gregarious, Docile, Willful, Friendly.

Height:
Male: 12-16 inches(31-40cm)
Female: 12-16 inches(31-40cm)

Cost: $1,500-$4,000.
___________________
|                 |
|                 |
|        |`-._ _  |
|        / `  _/  |
|        ****`    |
|       /    }    |
|      /  \ /     |
|  \ /`   \\\\\\     |
|   `\    /_\\\\    |
|    `~~~~~``~`   |
-------------------
----------------------------------------------------
""")

def web():
    print("""
For number 1 I typed in German Shepherd.
For number 2 I typed in Shih Tzu, then Shih Tzu cost.
for number 3 I typed in Golden Retriever. You can see a 3D model if on phone.
For number 4 I typed in Bulldog, then Bulldog cost.
""")

def breeds():
    while True:
        intro()
        choice = input("Pick an option 1,2,3,4,5,or 6 ")
        if choice == "1":
            Shepherd()
        if choice == "2":
            Shihtzu()
        if choice == "3":
            Gold()
        if choice == "4":
            Bull()
        if choice == "5":
            web()
        if choice == "6":
            quit()


