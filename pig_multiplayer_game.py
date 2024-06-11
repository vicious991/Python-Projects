import random 

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

while True:
    players = input("Enter The Number Of Players(2-4) :---- ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
            break
        else:
            print("please enter value between 2 and 4")
    
    else:
        print("INVALID INPUT")

max_score = 50
player_scores = [ 0 for _ in range(players)]

while max(player_scores) < max_score:
        
    for player_idx in range(players):
        print("\nplayer",player_idx + 1,"has just started:---\n")
        print("your toal score is :--" ,player_scores[player_idx])

        current_score = 0
        while True:

            should_roll= input("would you like to roll(y/n) ?--->").lower()
            if should_roll == "y":
                value = roll()
                if value == 1:
                    print("you rolled 1 ! turn done")
                    current_score = 0  
                    break

                else:
                    current_score += value
                    print("you rolled a:",value)
                
                print("your score is : ",current_score)
            else:
                break
        
        player_scores[player_idx] += current_score
        print("your total score is :",player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("The WINNER is player  :---> ", winning_idx + 1)

