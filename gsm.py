class gameStateManager():
    def __init__(self, current, alex):
        self.__currentState = current
        self.alex = alex
        self.result = ["None"]
        
    def setCurrentState(self, new):
        self.__currentState = new
        
    def getCurrentState(self):
        return self.__currentState