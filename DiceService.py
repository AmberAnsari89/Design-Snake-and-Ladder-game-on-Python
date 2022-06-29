import random
class DiceService:
    def __init__(self,numberOfDice):
        self._numberOfDice=numberOfDice

    def getNumberOfDice(self):
        return self._numberOfDice

    def roll(self):
        value=random.randint(1,6)*self._numberOfDice
        return value

    
