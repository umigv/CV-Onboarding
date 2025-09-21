"""
Class game
"""
from rich.text import Text
from rich.console import Console
import random

#Global objects
console = Console()


class Game():
    def __init__(self,rounds):
        self.rounds = rounds
       
    def check_roles(self,player1, player2) -> Text:
        intro_text = Text(justify="left")
        if player1.type == "host":
            intro_text.append(f"Let's welcome {player1.name}, he will be our host for this session.\n")
        else:
            intro_text.append(f"Let's welcome {player1.name}, he will be our player for this session.\n")

        if player2.type == "host":
            intro_text.append(f"Let's welcome {player2.name}, he will be our host for this session.\n")
        else:
            intro_text.append(f"Let's welcome {player2.name}, he will be our player for this session.\n")

        return intro_text
    
    def play_round(self,player,host):
        objects = ["car","goat","goat"]
        random.shuffle(objects)
        self.game_state = {f"Door {i+1}": prize for i, prize in enumerate(objects)}

        # Begin the game
        self.player_pick(player,host)
        self.host_pick(host, game_state=self.game_state)
        self.host_option(player,host,game_state=self.game_state)
        self.result(player,host,game_state=self.game_state)

    def player_pick(self,player,host):
        choice = int(input(f"So, {player.name}, which door will you pick? (1, 2 or 3): "))
        door_choice = f"Door {choice}"
        player.persona_pick(choice=door_choice)
        host.invalid.append(player.choices[-1])

    def host_pick(self,host,game_state):
        # doors left after the player's pick
        # Goes over dict, and excludes the door from the player's pick.
        remaining_doors = [door for door in game_state if door not in host.invalid]

        # host must pick one of the goats from remaining doors
        # This just ensures that from the two doors, it just saves goat doors.
        goat_doors = [door for door in remaining_doors if game_state[door] == "goat"]

        # host randomly chooses one goat door to reveal (so this takes care if there is only 1 goat, as in 1 car and 1 goat.)
        choice = random.choice(goat_doors)

        host.persona_pick(choice=choice)
        print(f"The {host.name} opens {choice}, and reveals a goat!")

    def host_option(self,player,host,game_state):
        print(f"The {host.name} tells you on your turn, would you like to switch or keep your door?")
        decision = input(f"So, {player.name} will you switch or keep? [switch/keep]: ")
        if decision == "switch":
            # find all doors
            all_doors = set(game_state.keys())

            # player’s current pick
            player_pick = player.choices[-1]

            # host’s revealed door
            host_pick = host.choices[-1]

            # the remaining unopened door (Set theory followed me to python, god dammit)
            remaining_door = (all_doors - {player_pick, host_pick}).pop()

            # switch to it 
            player.choices.append(remaining_door)
            print(f"{player.name} switches to {remaining_door}.")
        else:
            print(f"{player.name} keeps {player.choices[-1]}.")
        
    def result(self,player,host,game_state):
        player_choice = player.choices[-1]
        prize = game_state[player_choice]

        if prize == "car":
            print(f"Congratulations {player.name}, your door had a car and YOU WON!\n")
            player.wins += 1
        else:
            print(f"Uhmm {player.name}, your door had a goat, you lost, but gained a friend\n")


       