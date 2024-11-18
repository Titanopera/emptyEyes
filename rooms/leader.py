import room
import pygame
import time
clock = pygame.time.Clock()
class Leader(room.Room):
    def __init__(self, display, objects, gameStateManager) -> None:
        self.displays = display
        self.objects = objects
        self.gameStateManager = gameStateManager
        self.name = "fDrEeSePdAoImR"
        
    def run(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
            print(self.displays)
            self.displays.fill((0,0,0))
            if self.objects["leader_btn"].draw(self.displays):
                self.gameStateManager.setCurrentState("epilogue")
        pygame.display.flip()
        clock.tick(60)
            