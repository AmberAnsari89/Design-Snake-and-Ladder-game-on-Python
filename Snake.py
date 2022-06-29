class Snake:
    '''
        def __init__(self):
        self.snakeHeadTail={}

    def getPositionHead(self,head):
        if head in self.snakeHeadTail:
            return self.snakeHeadTail[head]
        else:
            return 0

    def setPositionHeadTail(self,head,tail):
        if head not in self.snakeHeadTail:
            self.snakeHeadTail[head]=tail
        return
    '''

    def __init__(self,start,end):
        self._start=start
        self._end=end

    def getStart(self):
       return self._start

    def getEnd(self):
       return self._end