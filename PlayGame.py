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