import pygame
import room
import npc
import text
clock = pygame.time.Clock()

class Mirror(room.Room):
    def __init__(self, display, result, objects, gameStateManager, homeRoom) -> None:
        super().__init__(display, result, objects, gameStateManager)
        self.base_font = pygame.font.Font(None, 32)
        self.homeRoom = homeRoom
        self.name = "shrine"
    
    def setRoom(self, newHomeRoom):
        self.homeRoom = newHomeRoom
        
    def run(self):
        if(self.result[-1]=="None"):
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                self.display.fill((0,0,0))
        