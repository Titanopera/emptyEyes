import room
import pygame
import time
clock = pygame.time.Clock()
class End(room.Room):
    def __init__(self, display, objects, gameStateManager) -> None:
        self.displays = display
        self.objects = objects
        self.gameStateManager = gameStateManager
        self.name = "fDrEeSePdAoImR"
        self.clicked = False
        self.base_font = pygame.font.Font(None, 32)
        
        
    def run(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
            self.displays.fill((23,34,78))
            if self.objects["eye_btn"].draw(self.displays):
                self.clicked =True
                print("The End")
            if(self.clicked == True):
                text_surface = self.base_font.render("The End.", True, (255,255,255))
                self.displays.blit(text_surface,(250,100))
                text_surface = self.base_font.render("Made By Titanopera for the 2024 Game Jam", True, (255,255,255))
                self.displays.blit(text_surface,(80,150))
        pygame.display.flip()
        clock.tick(60)