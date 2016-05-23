import re 

class PlayerNamePicker: 
    """Player name picker allows players to select their names and validates their entries when selecting the names.""" 
    def __init__(self): 
        pass 

    def selectPlayerOptions(self, gameMode):
        player1Name = self.selectPlayerName(1) 
        if gameMode == "Single Player Game": 
            player2Name = "Computer" 
        else: 
            player2Name = self.selectPlayerName(2) 
        playerNames = [player1Name, player2Name] 
        return playerNames

    def selectPlayerName(self, playerNumber): 
            nameInput = input("\nPlayer " + str(playerNumber) + ", please enter your name: ") 
            playerName = self.validatePlayerName(nameInput) 
            return playerName 

    def validatePlayerName(self, rawNameInput): 
        if len(rawNameInput) < 2: 
            print("\nPlayer name must contain 2 characters or more") 
            rawNameInput = input("\nPlease enter your name: ")
            return self.validatePlayerName(rawNameInput) 
        elif len(rawNameInput) > 20: 
            print("\nPlayer name must contain 20 characters or less") 
            rawNameInput = input("\nPlease enter your name: ") 
            return self.validatePlayerName(rawNameInput)
        elif re.match("^[a-zA-Z0-9\s]*$", rawNameInput): 
            return rawNameInput 
        else: 
            print("\nPlayer name must contain only letters, numbers, or spaces") 
            rawNameInput = input("\nPlease enter your name: ")
            return self.validatePlayerName(rawNameInput) 