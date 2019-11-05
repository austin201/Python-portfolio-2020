# Austin Daybell
# Top 20 video games

import random
top_games =["World of warcraft","Minecraft","Ark Survival",
            "Fallout 76","Madden19","FIFA16",
            "Jurassic World Evolution","BTD 2",
            "No Man's sky","Terraria","Star Wars Battlefront 2",
            "Mario","Last Day On Earth",
            "Rocket League","Tetris","Arcade Pacman",
            "Wii Sports","Super Mario Bros Wii",
            "Guitar Hero","Star Wars Battlefront"]

if "fortnite" in top_games:
    print("Fail")
elif top_games[0] != "World of warcraft":
    print("Fail")
else:
    print("Pass")
print(len(top_games))
for i in range(0,3):
    print(top_games[i])
randomnum = random.randint(0,len(top_games)-1)
print(top_games[randomnum])
top_games[0] = "World of warcraft"
            
if "fortnite" in top_games:
    print("Fail")
elif top_games[0] != "World of warcraft":
    print("Fail")
else:
    print("Pass")
print(len(top_games))
for i in range(0,3):
    print(top_games[i])
randomnum = random.randint(0,len(top_games)-1)
print(top_games[randomnum])
top_games[0] = "World of warcraft"


worst_games =["Fortnite","Candy Crush","
