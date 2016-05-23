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