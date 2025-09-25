import random
# Welcome message 
print("Welcome to Rock, Paper, Scissors!")
print()
game_over = False
round_num = 0
user_score = 0
comp_score = 0

# Repeat until game over
while game_over == False:
    round_num += 1
    print("Round ", round_num)
    # Prompt the user to type in their choice
    user_input = input("Please type in your choice out of Rock, Paper, and Scissors: ")
    # if invalid, repeat and ask again
    while (user_input != "Rock" and user_input != "Paper" and user_input != "Scissors"):
        user_input = input("Invalid input. Please type in 'Rock', 'Paper', or 'Scissors': ")
    #Generate a random response   
    #1 is rock, 2 is paper, 3 are scissors  
    response_int = random.randint(1, 3)
    if (response_int == 1):
        print("Your opponent chose Rock.")
    elif (response_int == 2):
        print("Your opponent chose Paper.")
    else:
        print("Your opponent chose Scissors.")
    print()
    #for each response, give the scenario for win and lose
    #if user inputs rock
    #current_status is 1 when draw, 2 when lose, 3 when win
    current_status = 0
    if (user_input == "Rock"):
        if (response_int == 1):
            current_status = 1
        elif (response_int == 2):
            current_status = 2
        else:
            current_status = 3   
    #if user inpputs paper
    elif (user_input == "Paper"):
        if (response_int == 2):
            current_status = 1
        if (response_int == 3):
            current_status = 2
        else:
            current_status = 3
    #if user inpputs scissors
    else:
        if (response_int == 3):
            current_status = 1
        if (response_int == 1):
            current_status = 2
        else:
            current_status = 3
    #print the result and change scores based on the current round results
    if current_status == 1:
        print("DRAW, +0")
    elif current_status == 2:
        print("YOU LOST, +0")
        comp_score += 1
    else:
        print("YOU WON, +1")
        user_score += 1
    print("Your current score is ", user_score, ".  Your opponent's score is ", comp_score, ".")
    print()
    play_again = input("Play again? Y for yes and N for no: ")  
    print()    
    #if input is neither 
    while play_again != 'Y' and play_again != 'N':
        play_again = input("Invalid input. Please type in 'Y' or 'N'.")
    if play_again == 'N':
        game_over = True
print("Your final score is ", user_score, ".  Your opponent's final score is ", comp_score, ".")
if (user_score > comp_score):
    print("Winner winner chicken dinner!!!")
elif (user_score == comp_score):
    print("Not losing is winning!!")
else:
    print("You win some, you lose some!")
print("Thank you for playing, hope to see you again soon!")