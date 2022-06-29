import SnakeAndLadderBoard
import Snake
import Ladder
import Player
import DiceService
from collections import deque

class SnakeAndLadderService:
    noOfDices=0
    shouldGameContinueTillLastPlayer=False
    shouldAllowMultipleDiceRollOnSix=False
    DEFAULT_BOARD_SIZE = 100
    DEFAULT_NO_OF_DICES = 1

    def __init__(self, boardSize):
        self.snakeAndLadderBoard=SnakeAndLadderBoard(boardSize)
        self.players=deque()
        self.noOfDices=SnakeAndLadderService.DEFAULT_NO_OF_DICES


    def setnoOfDices(self, noOfDices):
        self.noOfDices=noOfDices

    def setShouldGameContinueTillLastPlayer(self, shouldGameContinueTillLastPlayer):
        self.shouldGameContinueTillLastPlayer=shouldGameContinueTillLastPlayer

    def  setShouldAllowMultipleDiceRollOnSix(self, shouldAllowMultipleDiceRollOnSix):
        self.shouldAllowMultipleDiceRollOnSix=shouldAllowMultipleDiceRollOnSix

    def setPlayers(self,players):
        #self.players=deque()
        self.initialNumberOfPlayers=len(players)
        self.playerPieces={}
        for player in players:
            self.players.append(player)
            self.playerPieces[player.getId()]=0
        self.snakeAndLadderBoard.setPlayerPieces(self.playerPieces)

    def setSnakes(self,snakes):
            self.snakeAndLadderBoard.setSnakes(snakes)


    def setLadders(self, ladders):
        self.snakeAndLadderBoard.setLadders(ladders)

    def getNewPositionAfterGoingThroughSnakesAndLadders(self, newPosition):
        previousPosition=-1
        while previousPosition!=newPosition:
            previousPosition = newPosition
            for snake in self.snakeAndLadderBoard.getSnakes():
                if snake.getStart()==newPosition:
                    newPosition=snake.getEnd()

            for ladder in self.snakeAndLadderBoard.getLadders():
                if ladder.getStart()==newPosition:
                    newPosition=ladder.getEnd()

        return newPosition

    def movePlayer(self,player,positions):
        oldPosition = self.snakeAndLadderBoard.getPlayerPieces().get(player.getId())
        newPosition = oldPosition + positions

        boardSize = self.snakeAndLadderBoard.getBoardSize()

        if (newPosition > boardSize):
            newPosition = oldPosition

        else:
            newPosition = self.getNewPositionAfterGoingThroughSnakesAndLadders(newPosition)

        self.snakeAndLadderBoard.getPlayerPieces()[player.getId]=newPosition
        print(player.getName() + " rolled a " + positions + " and moved from " + oldPosition + " to " + newPosition)


    def getTotalValueAfterDiceRolls(self):
            # Can use noOfDices and setShouldAllowMultipleDiceRollOnSix here to get total value (Optional requirements)
            return DiceService.roll();

    def hasPlayerWon(self, player):
            #Can change the logic a bit to handle special cases when there are more than one dice (Optional requirements)
            playerPosition = self.snakeAndLadderBoard.getPlayerPieces().get(player.getId());
            winningPosition = self.snakeAndLadderBoard.getSize();
            return playerPosition == winningPosition

    def isGameCompleted(self):
            #Can use shouldGameContinueTillLastPlayer to change the logic of determining if game is completed (Optional requirements)
            currentNumberOfPlayers = self.players.size()
            return currentNumberOfPlayers < self.initialNumberOfPlayers

    def startGame(self):
        while not self.isGameCompleted():
            totalDiceValue = self.getTotalValueAfterDiceRolls() # Each player rolls the dice when their turn comes.
            currentPlayer = self.players.leftpop();
            self.movePlayer(currentPlayer, totalDiceValue);
            if (self.hasPlayerWon(currentPlayer)):
                print(currentPlayer.getName() + " wins the game");
                self.snakeAndLadderBoard.getPlayerPieces().remove(currentPlayer.getId());
            else:
                self.players.add(currentPlayer);


