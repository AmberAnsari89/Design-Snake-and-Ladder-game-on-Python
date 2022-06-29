import uuid


class Player:
    '''
    def __init__(self,numberOfPlayer):
        self._listOfPlayer=[numberOfPlayer]

    def setPlayerName(self,player,number):
        self._listOfPlayer[number]=player
    '''
    def __init__(self,name):
        self._name=name
        self._id=str(uuid.uuid1())

    def getName(self):
        return self.name

    def getId(self):
        return self.id

  

