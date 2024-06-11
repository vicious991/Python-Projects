import random 

guesses = 0

while True:
    guesses += 1
    top_of_range = int(input("type a number :--- "))
    
    if top_of_range <= 0:
        print("enter a number larger than 0")
        quit()

    random_number = random.randint(0,top_of_range) # from 0 to 10 # randrange icludes 0 to 9
    
    if top_of_range == random_number:
        print("you guessed correctly")
        break
    elif top_of_range > random_number:
        print("you were above the number")

    else:
        print("you were below the number")       

print(f"you got it in {guesses} guesses")