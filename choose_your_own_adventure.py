name = input("Type your name :--- ")
print(f"welcome {name} to this adventure !!!!")

input1 = input("you are on a turn choose between left or right:--- ").lower()

if input1 == "left":
    input2= input("there is a bridge over  sea you wanna 'swim' or 'walk' across it:--- ")
    if input2 == "swim":
        print("there was a crocodile you were eaten:--- ")
        print("you Lost")
        quit()

    elif input2 == "walk":
        print("you reached your destination:--- ")
        print(" you Won")
        quit

    else:
        print("INVALID INPUT")


elif input1 == "right":
    input3 = ("there is a mountain go 'around' it or 'trek' over it:--- ")
    if input3 == "around":
        print("you fell off the cliff you died:--- ")
        print("you lost")

    elif input3 == "trek":
        print("you are home you won:--- ")
        quit()

    else:
        ("INVALID INPUT")

else:
    print("INVALID INPUT")
    print("YOU LOST")
print(f" THANKS FOR PLAYING THE GAME {name}")