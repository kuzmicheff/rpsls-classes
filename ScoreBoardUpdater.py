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