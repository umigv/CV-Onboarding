"""
Monty Hall Game
Author: steffano@umich.edu
"""

from persona import Persona
from game import Game
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

#Global settings
console = Console()
game = Game(rounds=3) # Game set to 3.

def main():
    greet_user()
    player,host = initialize_personas()
    being_games(player,host)
    
    
def greet_user():
    """
    Text greetings, using the rich library :)
    """
    panel = Panel(Text("Welcome to the Monty Hall Show",justify="center"),title="Monty Hall Show",padding=(2,4))
    console.print(panel)
    panel = Panel(Text("In this game, there are 3 doors, and, behind each door, you have either a car or a goat, but there only exist 1 car, and 2 goats, will you pick the right door and win a car?",justify="center"),title="Monty Hall Show",padding=(2,4))
    console.print(panel)
    
def initialize_personas() -> None:
    """
    Creates the 2 people involved.
    """

    player_name = input("What is the player's name?: ")
    player_role = "player" # fixed
    host_name = "Sketchy Host"
    host_role = "host" 

    player = Persona(player_name,player_role)
    host = Persona(host_name,host_role)
    intro = game.check_roles(player,host)
    introduction_text = intro
    panel = Panel(introduction_text, title="Monty Hall Show", padding=(1))
    console.print(panel)

    return player,host

def being_games(player,host) -> None:
    panel = Panel(Text("You will play this game 3 times, you only win by getting 2 wins, good luck (or is it?)",justify="center"),title="Monty Hall Show",padding=(2,4))
    console.print(panel)

    # Lets play 1 game
    for round in range(game.rounds):
        game.play_round(player=player,host=host)
        if player.wins == 2:
            print("You won! What did you figure out was the best strategy?")
            break
        elif player.wins == 0 and round == 2:
            print("You lost, sorry.")



if __name__ == "__main__":
    main()