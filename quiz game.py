print("Welcome to my computer quiz!!!")
score = 0
playing = input("DO You Want To Play?: ").lower()

if playing != "yes":
    quit()
else:
    print("OKAY LET PLAY:)")

answer1 = input (" what does CPU stand for ? ").lower()
if answer1 == "central processing unit":
    score += 1
    print("correct!!")
else:
    print("wrong answer")

answer2 = input (" what does gpu stand for ? ").lower()
if answer2 == "graphics processing unit":
    score += 1
    print("correct!!")
else:
    print("wrong answer")


answer3 = input (" who own's twitter now x ? ").lower()
if answer3 == "elon musk":
    score += 1
    print("correct!!")
else:
    print("wrong answer")


answer4 = input (" who's the CEO of microsoft ? ").lower()
if answer4 == "satya nandella":
    score += 1
    print("correct!!")
else:
    print("wrong answer")


answer5 = input (" what is an IEM ?").lower()
if answer5 == "in ear monitor":
    score += 1
    print("correct!!")
else:
    print("wrong answer")


print(f"you got {score} out of 5 correct")
print(f"you got {score/5*100} percentile")
