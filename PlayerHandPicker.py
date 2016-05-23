import re

class PlayerHandPicker: 
    """docstring for PlayerHandPicker""" 
    def __init__(self): 
        pass 

    def selectPlayerHand(self, currentPlayerName):
        print("\nPlease select your hand") 
        handInput = input("\n" + currentPlayerName + ", press any key from 1 to 5: ") 
        playerHand = self.validatePlayerHand(handInput)
        print("\033c") 
        return playerHand 

    def validatePlayerHand(self, rawHandInput): 
        if re.match("^[1-5]$", rawHandInput): 
            rawHandInput = int(rawHandInput) 
            return rawHandInput 
        else: 
            rawHandInput = input("\n" + "Please press any key from 1 to 5: ")
            return self.validatePlayerHand(rawHandInput) 