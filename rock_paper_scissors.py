import random

# Create the game
class RockPaperScissors:
    
    def __init__(self, total_rounds = None):
        
        self.total_rounds = total_rounds
        self.game_over = False
        self.round_num = 1
        self.points = 0
        self.comp_points = 0
        self.user_input = None
    
    #play until it is over, once all rounds are played
    def start(self):
        
        #ask the user how many rounds they want to play. Type shi
        total_rounds_string = input("How many rounds of Rock, Paper Scissors would you like to play good sir/ma'am? Enter an integer number, pretty please: ")
        while total_rounds_string.isdigit() == False:
            total_rounds_string = input("Oops! That is most definitely not an integar value. Please try again, or else you will not be able to play this game!!!")
        self.total_rounds = int(total_rounds_string)
       
        # Main game loop
        while self.round_num  <= self.total_rounds:
            print("Round", self.round_num)
            #ask which option the user would like to pick()
            self.user_input = self.ask_user()
            #calculate score from random computer input type shi
            self.calculate_score()
            self.round_num += 1


        if(self.points > self.comp_points):
            print("You got", self.points, "point(s)! You're opponent got", self.comp_points, "point(s)! You beat them, you win!")
        if(self.points < self.comp_points):
            print("You got", self.points, "point(s)! You're opponent got", self.comp_points, "point(s)! You lost, oh well!")
        if(self.points == self.comp_points):
            print("You got", self.points, "point(s)! You're opponent got", self.comp_points, "point(s)! You guys tied! You are both as talented at rock, paper, scissors.")
    
    
    def ask_user(self):
        
        #ask which option the user would like to pick
        user_input = input("Choose your weapon: Rock, Paper, or Scissors (Capitalized): ")
        #if invalid response
        while(user_input != "Scissors" and user_input != "Paper" and user_input != "Rock"):
            user_input = input("Invalid response, please try again: ")
        return user_input

    def calculate_score(self):
        
        # 1 = Rock, 2 = Paper, 3 = Scissors
        computer_input = random.randint(1, 3)
        computer_input_string = None
        # Assign string values
        if(computer_input == 1):
            computer_input_string = "Rock"
        if(computer_input == 2):
            computer_input_string = "Paper"
        if(computer_input == 3):
            computer_input_string = "Scissors"
        # Losing cases
        if (self.user_input == "Scissors" and computer_input_string == "Rock" ):
            self.comp_points += 1
            print("You picked: ", self.user_input, ". Your opponent picked: ", computer_input_string, ". Your opponent got a point.", sep="")
        elif (self.user_input == "Rock" and computer_input_string == "Paper"):
            self.comp_points += 1
            print("You picked: ", self.user_input, ". Your opponent picked: ", computer_input_string, ". Your opponent got a point.", sep="")
        elif (self.user_input == "Paper" and computer_input_string == "Scissors"):
            self.comp_points += 1
            print("You picked: ", self.user_input, ". Your opponent picked: ", computer_input_string, ". Your opponent got a point.", sep="")
        elif (self.user_input == computer_input_string):
            print("You picked: ", self.user_input, ". Your opponent picked: ", computer_input_string, ". It was a draw", sep="")
        else:
            self.points += 1
            print("You picked: ", self.user_input, ". Your opponent picked: ", computer_input_string, ". You got a point.", sep="")

# Start the fireworks
RPS = RockPaperScissors()
RPS.start()