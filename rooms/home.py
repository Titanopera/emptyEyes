import pygame
import room
class Home(room.Room):
    def __init__(self, display, result, objects, gameStateManager) -> None:
        super().__init__(display, result, objects, gameStateManager)
        self.base_font = pygame.font.Font(None, 16)
        self.starter_text = "I open the store, I buy the Hero's goods, I close the store, I cry "
            
    def run(self):
            self.display.fill((0,0,0))
            text_surface = self.base_font.render(self.starter_text, True, (255,255,255))
            for i in range(0, 450, 5):
                self.display.blit(text_surface,(150+i,100+i))
            #Create the text box class