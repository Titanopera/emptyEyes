import pygame
clock = pygame.time.Clock()

class textBox():
    def __init__(self, display, speed, text, font, gameState):
        self.surface = display
        self.text = text
        self.font = font
        self.speed = speed
        self.gameState = gameState
        self.text_in_progress = True
        self.counter = 0
        #Draw the text a bit at a time.
        
        
            #This then chains into the next text Box. maybe create a linked list class
            
    def run(self):
        while(True):
            #This draws the black background and the white box.
            self.surface.fill((0,0,0))
            pygame.draw.rect(self.surface, "white", (0, 500, 600, 100), 2)
            if(self.text_in_progress):
                        current_text = self.font.render(self.text[0:self.counter//self.speed], True, (255,255,255))
                        self.surface.blit(current_text, (10, 510))
                        self.counter += 1
            else:
                    self.surface.blit(self.font.render(self.text, True, (255,255,255)),(10,510))
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_RETURN):
                        self.text_in_progress = False 
                elif(self.counter >= self.speed*len(self.text)):
                    self.text_in_progress = False 
                
                    #Set up an if statement that checks if the enter key is pressed 
                    # if so it moves on to the room pointed next in the linked list
            pygame.display.flip()
            clock.tick(60)