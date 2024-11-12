import pygame
import room

class Menu(room.Room):
    def __init__(self, display, objects, gameStateManager, result) -> None:
        super().__init__(display, objects, gameStateManager, result)
        self.base_font = pygame.font.Font(None, 32)
        self.starter_text = "Empty Eyes Can Still Dream" 
    
    def run(self):
        self.display.fill((23,34,78))
        text_surface = self.base_font.render(self.starter_text, True, (255,255,255))
        self.display.blit(text_surface,(150,100))
        if self.objects["start_btn"].draw(self.display):
            #Move to the first room.
            print("Start Clicked")
            self.gameStateManager.setCurrentState("home")
        if self.objects["end_btn"].draw(self.display):
            print("End Clicked")
            pygame.quit()
        if self.objects["eye_btn"].draw(self.display):
            print("Eye Clicked")
            #Nothing more done just a little easter egg that the image is secretely a button.
    