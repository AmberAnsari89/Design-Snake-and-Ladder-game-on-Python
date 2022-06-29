class SnakeAndLadderBoard:
    def __init__(self,boardSize):
        self._boardSize=boardSize
        self._snakes=[]
        self._ladders=[]
        self._playerPieces={}

    def getBoardSize(self):
        return self._boardSize

    def getSnakes(self):
        return self._snakes

    def  setSnakes(self,snakes):
        self._snakes=snakes

    def getLadders(self):
        return self._ladders

    def setLadders(self,ladders):
        self._ladders=ladders

    def getPlayerPieces(self):
        return self._playerPieces

    def setPlayerPieces(self,players):
        self._playerPieces=players