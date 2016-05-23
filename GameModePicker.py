import re 

class GameModePicker: 
    """Game mode picker allows players to select the game mode and validates their entries when selecting the mode.""" 

    def __init__(self):
        pass 

    def selectGameMode(self): 
        print("\nTo play against the computer, press 1 \nTo play against another player, press 2") 
        modeInput = input("\nPlease select the game mode: ") 
        modeInput = self.validateGameMode(modeInput) 
        if modeInput == "1": 
            gameMode = "Single Player Game" 
        else: 
            gameMode = "Multi Player Game"
        return gameMode 

    def validateGameMode(self, rawModeInput): 
        if re.match("^[12]$", rawModeInput): 
            return rawModeInput 
        else: 
            rawModeInput = input("\nPlease press 1 or 2: ")
            return self.validateGameMode(rawModeInput) 