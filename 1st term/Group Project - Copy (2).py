#Group Project
#Seth Jones
#Austin daybell
#Jacob cook
#Noah Hancock

#run time error: using letter inputs instead of numbers, logic error in circle with ascii art getting skewed, logic error volume cannot be negitive

        
def intro():
    print("""
    Welcome to the math operator for area and perimeter of a
    square,area of triangle, volume of cube, and circumference of circle.
    You may choose what you need below.

    1. cube
    2. square
    3. triangle
    4. circle
    5. leave
        """)

ft = "ft."
def cube():
    cubeLength = input("Enter your length, width, or height in feet: ")

    cubeResult = float(cubeLength) **3

    cubeEquals = str.format("""
     @ + + + + + + + + + + + @
     +\\                      +\\
     + \\                     + \\
     +  \\                    +  \\
     +   \\                   +   \\
     +    @ + + + + + + + + +++ + @
     +    +                  +    + 
     +    +                  +    +
     +    +                  +    +
     +    +                  +    +
     +    +                  +    +
     +    +                  +    +
     @ + +++ + + + + + + + + @    +
      \\   +                   \\   +
       \\  +                    \\  +
        \\ +                     \\ +
         \\+                      \\+
          @ + + + + + + + + + + + @
    length/width/height: {0}
                     
     your volume is {1} {2}""",cubeLength,round(cubeResult,2),ft+"^3")

    print(cubeEquals)

#square
def square():
    type_square= input("Enter length or width in feet: ")
    square= float(type_square)

    perim = square*4
    area = square**2
    squareAskie = str.format("""
    NNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMW
    NWMMMMMMMMMMMMMMMMWNNWWMMMMMMMMMMMMMMWNX  length/width: {0}
    NWMMMMMMMMMMMMMMMMWWWWMMMMMMMMMMMMMMMWNX
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN
    NXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

     your perimeter is {1} {2}
    and your area is {3} {2}^2
    """, type_square,round(perim,2),ft,round(area,2))
    print(squareAskie)

#triangle
def triangle():
    tri_base_type= input("Enter base in feet: ")
    tri_height_type= input("Enter height in feet: ")
    tri_base = float(tri_base_type)
    tri_height = float(tri_height_type)
    tri_total = tri_height*tri_base/2
    triangle = str.format("""
                     M
                    NWM
                   KKXGS
                  KKK0KNM
                 KKK000KNW
                K0KKKKKKKNW
               KKKKKK0KKKKXW
              KKK0KKK0KKKKKNW
             KKKKKKKKKKKKK0KNW
            KKK0KKKKK00KKKK0KNW   height: {0}
           0KK0000KKK00KKKKK0KXW
          KKKKKK0KKKKKKKKKK0KKKXW
         KK0KKKK00KKK00KKKK0KKKKXM
        KKKKKKKKKKKKK00KKKKKKKKK0XW
       KKKKKKKKKKKKKK00KKKKKKKK00KXM
      0KKKK0KKKK0KKKK00KKKK0KKK00KKNM
     KKKKKK0KKKKKKKKK000KK0KKKKK0KKKKM
    KK0KXKKKXKKKXXXXXXXXXXXXXXXXXXXXXNM
                 base: {1}

     your area is {2}""",tri_height,tri_base, round(tri_total,2))
    print(triangle)

def circle():
    circumferanceAngle = input("Enter your radius in feet: ")
    Pie = 3.14

    circumferanceEquals = 2.0 *Pie* float(circumferanceAngle)

    circle = str.format("""

               %%%    %%%
          %%%              %%%

      %%%                      %%%

     %%%  radius: {0}            %%%
        -------------
     %%%                         %%%

      %%%                       %%%

       %%%                     %%%

               %%%    %%%

     your circumferance is {1} {2}""",circumferanceAngle,round(circumferanceEquals,2), ft)


    print(circle)


def leave():
    while True:
        varify = input("Are you sure you want to leave ")
        if varify == "yes":
            return True
        elif varify == "no":
            return False
        else:
            print("Not a good response")
            continue

def answer():
    while True:
        intro()
        choice = input("Pick an option 1,2,3,4,or 5 ")
        if choice == "1":
            cube()
        if choice == "2":
            square()
        if choice == "3":
            triangle()
        if choice == "4":
            circle()
        if choice == "5":
            quit()

pwords = "Shadow, Shadow42364, Shadowdog42364"
userNames = "Austin, Kevin, Mason, Malinda, Kenzie, Kylee, Kayden, Kyler, Kaylene, Auntie, Alicia, Kent"

uninput = input("Enter your name, capitalize first letter: ")
password = input("Enter your password ")
if (uninput in userNames) and (password in pwords) and (password != "password") or (uninput in "allowed"):
    print("You got in")
    answer()

elif uninput not in userNames:
        print("Incorrect Username")
else:
    print("Incorrect Password")
    

