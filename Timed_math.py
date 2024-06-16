import random
import time

OPERATORS = ["+","-","*"]              # this are the various operations
min_value= 2                           # minimum value to put in poblem
max_value = 12                         # maximum value
total_questions = 5                    # total no of questions



def generate_problem():                # class for generating problem
    left = random.randint(min_value,max_value) # random module to use random no between  2 - 12
    right = random.randint(min_value,max_value)
    operator = random.choice(OPERATORS)
    
    question = str(left) + " " + operator + " "+str(right)  # formulating the string
    answer = eval(question)
    return question , answer     # returning the value

start = input("Press Enter To Start:--")
start_time= time.time()
print("---------------------------------")

for i in range(total_questions): 
    question,answer = generate_problem()
    while True:
        guess = input(f"Question No. {i+1} :" + question + " = ") # taking input from the user
        if int(guess) == int(answer):
            print("Correct Answer !!!!")
            break
        else:
            print("Incorrect Answer!!!!")

end_time = time.time()
print("----------------------------------")

total_time = round(end_time- start_time,2) # calculating the total no of time taken
print(f"Good work !!!! you finished it in {total_time} Seconds!!!") # final statement


