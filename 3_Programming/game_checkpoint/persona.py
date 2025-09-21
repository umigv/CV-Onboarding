"""
Persona Object
"""


class Persona:
    """
    This will control each person's decision and type.
    """
    def __init__(self, name: str,role: str):
        """
        Instanciates the class to either be:
        1. The name of the person.
        2. The role,
            - A player 
            - A host
        """
        self.name = name
        self.type = role 
        self.choices = []
        self.invalid = []
        self.wins = 0

    def persona_pick(self,choice: int):
        self.choices.append(choice)
        

    
   





        