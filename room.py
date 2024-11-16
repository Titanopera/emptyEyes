import pygame
import gsm
class Room():
    def __init__(self, display, result, objects, gameStateManager) -> None:
        self.display = display
        self.objects = objects
        self.gameStateManager = gameStateManager
        self.result = []
        self.result.append(result)
        
    def run(self):
        self.display.fill((0,0,0))
        
