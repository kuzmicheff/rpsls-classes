import re

class NextRoundPicker: 
    """docstring for NextRoundPicker"""
    def __init__(self): 
        pass 

    def playNextRound(self, ):
        print("\nWould you like to play another round?") 
        nextRoundChoice = input("Please press y or n on the keyboard: ") 
        nextRoundChoice = self.validateNextRoundInput(nextRoundChoice) 
        return nextRoundChoice

    def validateNextRoundInput(self, nextRoundInput):
        if re.match("^[yn]$", nextRoundInput): 
            return nextRoundInput 
        else: 
            nextRoundInput = input("Please press y or n to continue or stop: ") 
            return self.validateNextRoundInput(nextRoundInput) 