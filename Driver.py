import Snake
import Ladder
import Player
import SnakeAndLadderService
if __name__=="__main__":
    noOfSnakes=input().strip()
    snakes=[]
    for i in range(noOfSnakes):
        snakes.append(Snake(input().strip(),input().strip()))

    noOfLadders = input().strip()
    ladders = []
    for i in range(noOfLadders):
        ladders.append(Ladder(input().strip(), input().strip()))

    noOfPlayers = input().strip()
    players = []
    for i in range(noOfPlayers):
        players.append(Player(input().strip()))

    snakeAndLadderService=SnakeAndLadderService()
    snakeAndLadderService.setPlayers(players)
    snakeAndLadderService.setSnakes(snakes)
    snakeAndLadderService.setLadders(ladders)

    snakeAndLadderService.startGame()