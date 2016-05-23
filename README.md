# Task: rpsls-classes 

This version of the game of rock, paper, scissors, lizard, Spock in Python 3 uses classes and consists of the following files. The game starts by running __main__.py from the command line which calls PlayGame.py that contains the main game flow function and calls the rest of classes. 

## Classes

0. main.py 
0. PlayGame.py 
0. GameModePicker.py 
0. PlayerNamePicker.py 
0. PlayerHandPicker.py 
0. RoundResultCalculator.py 
0. NextRoundPicker.py 
0. ScoreBoardUpdater.py 

--- 

### File: main.py 

This file imports the PlayGame class and calls the main game flow. 

#### Code 

``` 
from PlayGame import PlayGame 

def main(): 
    
    game = PlayGame() 
    game.startPlayingGame() 
    

if __name__ == "__main__": 
    main() 
``` 

--- 

### File: PlayGame.py 

This file imports the rest of classes, allows the user to choose the game mode and player names. As soon as the pre-game data gets collected and verified, the file starts a new round and continues to play consecutive rounds while keeping the total score. The user can select whether to continue playing or not at the end of each round. When the game finishes, the total score displays on the screen. 

#### Code 

``` 
import random

from GameModePicker import GameModePicker 
from PlayerNamePicker import PlayerNamePicker 
from PlayerHandPicker import PlayerHandPicker 
from RoundResultCalculator import RoundResultCalculator 
from NextRoundPicker import NextRoundPicker
from ScoreBoardUpdater import ScoreBoardUpdater 

class PlayGame: 
    """Game play allows players to select their hands and figures the winner of each round.""" 

    def __init__(self): 
        self.gameTitle = "\nGame of Rock, Paper, Scissors, Lizard, Spock" 
        self.gameRules = "\nKeyboard keys and game rules: \n\n1: Scissors cuts Paper (2) and decapitates Lizard (4) \n2: Paper covers Rock (3) and disproves Spock (5) \n3: Rock crushes Scissors (1) and crushes Lizard (4) \n4: Lizard eats Paper (2) and envenomates Spock (5) \n5: Spock vaporizes Rock (3) and smashes Scissors (1)" 

    def displayTitleRules(self):
        print(self.gameTitle) 
        print(self.gameRules)

    def startPlayingGame(self): 
        titleAndRules = self.displayTitleRules()
        modeInput = GameModePicker() 
        gameMode = modeInput.selectGameMode()
        print("\033c")
        print(gameMode) 
        playerInput = PlayerNamePicker() 
        playerNames = playerInput.selectPlayerOptions(gameMode) 
        print(playerNames)
        gameScore = [0, 0] 
        print("\033c") 
        print(gameMode)
        print("\n" + playerNames[0], str(gameScore[0]) + ":" + str(gameScore[1]), playerNames[1]) 
        newRoundScore = self.playNewRound(gameMode, playerNames, gameScore) 
        gameFinalScore = ScoreBoardUpdater() 
        finalScore = gameFinalScore.displayFinalScore(playerNames, newRoundScore) 

    def playNewRound(self, currentMode, currentPlayers, currentScore): 
        player1HandInput = PlayerHandPicker() 
        player1HandPick = player1HandInput.selectPlayerHand(currentPlayers[0]) 
        if currentMode == "Single Player Game": 
            gameHands = [1, 2, 3, 4, 5] 
            player2HandPick = random.choice(gameHands) 
        else: 
            player2HandInput = PlayerHandPicker() 
            player2HandPick = player2HandInput.selectPlayerHand(currentPlayers[1]) 
        newRoundResult = RoundResultCalculator()
        roundResult = newRoundResult.calculateRoundResult(player1HandPick, player2HandPick) 
        roundScore = ScoreBoardUpdater() 
        totalScore = roundScore.updateScoreBoard(roundResult, currentPlayers[0], currentPlayers[1], player1HandPick, player2HandPick, currentScore[0], currentScore[1]) 
        print("\n" + currentPlayers[0], str(totalScore[0]) + ":" + str(totalScore[1]), currentPlayers[1])
        nextRoundInput = NextRoundPicker() 
        nextRoundPick = nextRoundInput.playNextRound() 
        if nextRoundPick == "y": 
            print("\033c") 
            return self.playNewRound(currentMode, currentPlayers, totalScore) 
        else: 
            print("\033c") 
            return totalScore 
``` 

--- 

### File: GameModePicker.py 

This file allows user to select the game mode. If the user selects 1, the game is played against computer. If the user selects 2, the game is played against another player. The input from user is validated prior to be returned to the main game flow. 

#### Code 

``` 
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
``` 

--- 

### File: PlayerNamePicker.py 

This file allows users to select their names and validate user inputs. The player name in this game must be from 2 to 20 characters in length and contain letters, numbers, and spaces. In a single player game, the second player is automatically assigned *Computer" as the player name. 

#### Code 

``` 
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
``` 

--- 

### File: PlayerHandPicker.py 

This file allows each player to select their hand for each round in the game. The user input is validated and returned to the main game flow for calculating the result of the round. 

#### Code 

``` 
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
``` 

--- 

### File: RoundResultCalculator.py 

This file calcualtes whether the last played round is a win by either player or tie. It returns the round result as a string. 

#### Code 

``` 
class RoundResultCalculator:
    """docstring for RoundResultCalculator"""
    def __init__(self):
        pass 

    def calculateRoundResult(self, player1HandPick, player2HandPick): 
            if (player2HandPick - player1HandPick) % 5 in (1, 3): 
                roundResult = "Player 1" 
            elif (player2HandPick - player1HandPick) % 5 in (2, 4): 
                roundResult = "Player 2" 
            else: 
                roundResult = "Tie" 
            return roundResult 
``` 

--- 

### File: NextRoundPicker.py 

This file allows the user to play consecutive rounds and validates the input. If the user selects *y* at the end of the round, the new round starts. If the user select *n*, the game prints the total score and exits. 

#### Code 

``` 
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
``` 

--- 

### File: ScoreBoardUpdater.py 

This file prints status messages after each round. It shows what hands users selected, what result the round ended with, and the updated total score. This file also prints the total score at the end of the game. 

#### Code 

``` 
class ScoreBoardUpdater:
    """Score board keeps the total score between players as the game proceeds through multiple rounds."""
    def __init__(self):
        pass 

    def updateScoreBoard(self, result, player1, player2, hand1, hand2, score1, score2):
        handTitleList = ["Scissors", "Paper", "Rock", "Lizard", "Spock"] 
        handMessageList = ["Scissors (1) cuts Paper (2)", "Paper (2) covers Rock (3)", "Rock (3) crushes Lizard (4)", "Lizard (4) poisons Spock (5)", "Spock (5) smashes Scissors (1)", "Scissors (1) decapitates Lizard (4)", "Lizard (4) eats Paper (2)", "Paper (2) disproves Spock (5)", "Spock (5) vaporizes Rock (3)", "Rock (3) crushes Scissors (1)"]
        handTitle1 = handTitleList[hand1 - 1] 
        handTitle2 = handTitleList[hand2 - 1] 
        print(player1 + " selected " + handTitle1 + "(" + str(hand1) + ")") 
        print(player2 + " selected " + handTitle2 + "(" + str(hand2) + ")") 
        if (hand1 == 1 and hand2 == 2) or (hand1 == 2 and hand2 == 1): 
            print("\n" + handMessageList[0]) 
        elif (hand1 == 2 and hand2 == 3) or (hand1 == 3 and hand2 == 2): 
            print("\n" + handMessageList[1]) 
        elif (hand1 == 3 and hand2 == 4) or (hand1 == 4 and hand2 == 3): 
            print("\n" + handMessageList[2]) 
        elif (hand1 == 4 and hand2 == 5) or (hand1 == 5 and hand2 == 4): 
            print("\n" + handMessageList[3]) 
        elif (hand1 == 5 and hand2 == 1) or (hand1 == 1 and hand2 == 5): 
            print("\n" + handMessageList[4]) 
        elif (hand1 == 1 and hand2 == 4) or (hand1 == 4 and hand2 == 1): 
            print("\n" + handMessageList[5]) 
        elif (hand1 == 4 and hand2 == 2) or (hand1 == 2 and hand2 == 4): 
            print("\n" + handMessageList[6]) 
        elif (hand1 == 2 and hand2 == 5) or (hand1 == 5 and hand2 == 2): 
            print("\n" + handMessageList[7]) 
        elif (hand1 == 5 and hand2 == 3) or (hand1 == 3 and hand2 == 5): 
            print("\n" + handMessageList[8]) 
        elif (hand1 == 3 and hand2 == 1) or (hand1 == 1 and hand2 == 3): 
            print("\n" + handMessageList[9]) 
        else: 
            print("\nPlayers picked the same hand") 
        if result == "Player 1": 
            print("\n" + player1 + " is the winner!") 
            score1 += 1 
        elif result == "Player 2": 
            print("\n" + player2 + " is the winner!") 
            score2 += 1 
        else: 
            print("\nThe game is tied!") 
        updatedScore = [score1, score2] 
        return updatedScore 

    def displayFinalScore(self, currentPlayers, finalScore): 
        print("Game over!\n\n" + currentPlayers[0], str(finalScore[0]) + ":" + str(finalScore[1]), currentPlayers[1] + "\n")
``` 

--- 

## Author's notes 

This version plays well, and its classes are nicely separated. I will, however, revise the naming for variables as I become more advanced in the use of classes in Python 3. 