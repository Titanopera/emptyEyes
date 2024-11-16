import pygame
import room
import npc
import text
clock = pygame.time.Clock()

class Shrine(room.Room):
    def __init__(self, display, result, objects, gameStateManager, homeRoom) -> None:
        super().__init__(display, result, objects, gameStateManager)
        self.base_font = pygame.font.Font(None, 32)
        self.homeRoom = homeRoom
        self.name = "shrine"
    
    def setRoom(self, newHomeRoom):
        self.homeRoom = newHomeRoom
        
    def run(self):        
        while(True):
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
            #Write Out The Shrine
            if self.objects["shrine_btn1"].draw(self.display):
                #Move to the first room.
                print("Shrine Clicked")
                self.gameStateManager.setCurrentState("home")            
                return
            if self.objects["shrine_btn2"].draw(self.display):
                #Move to the first room.
                print("Shrine Clicked")
                self.gameStateManager.setCurrentState("home")            
                return
            if self.objects["shrine_btn3"].draw(self.display):
                #Move to the first room.
                print("Shrine Clicked")
                self.gameStateManager.setCurrentState("home")            
                return
            pygame.display.flip()
            clock.tick(60)
            self.display.fill((0,0,0))
        