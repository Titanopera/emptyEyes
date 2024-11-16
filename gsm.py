class gameStateManager():
    def __init__(self, current):
        self.__currentState = current
        self.result = ["None"]
        
    def setCurrentState(self, new):
        self.__currentState = new
        
    def getCurrentState(self):
        return self.__currentState