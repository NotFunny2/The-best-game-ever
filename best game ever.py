# poop game

# ask the name and prints some stuff
ans = ""
print("Narrator: You are on some guys basement")
name = input("Your kidnapper: Welcome to my basement whats your name?: ")
print (f"Thats a stupid name, anyway {name}, wha- *The fbi enters the basement you where in*")

# the end of the game, has errors im to lazy to fix

while ans not in ["kill them", "kill my kidnapper"]:
    ans = input("what do you do? kill them or kill your kidnapper? (type kill them or kill my kidnapper): ").lower()


if ans in ["kill them", "kill my kidnapper"]:
    if ans == "kill them":
        print("After killing the fbi you and your kidnapper start dancing until you pass out for lack of slepping")

    elif ans == "kill my kidanpper":
        print("The fbi kills you cause they are bored lmao")

# the pain is over yayyyyyyyyyyy
input("The game is over go awayyyyyyyyyyyyyyyyyyyyyyyyyyy")
