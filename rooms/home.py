import pygame
import text
import time
clock = pygame.time.Clock()

class Home():
    def __init__(self, display, result, objects, gameStateManager) -> None:
        self.display = display 
        self.result = ["None"]
        self.name = "home"
        self.result.append(result)
        self.objects = objects
        self.gameStateManager = gameStateManager
        self.base_font = pygame.font.Font(None, 16)
        self.starter_text = "I open the store, I buy the Hero's goods, I close the store, I cry "
            
    def run(self):
        counter = 0
        if(self.result[0] == "None"):
            while(True):
                self.display.fill((0,0,0))
                text_surface = self.base_font.render(self.starter_text, True, (255,255,255))
                if(counter <= 5):
                    for i in range(counter):
                        time.sleep(1/counter)
                        self.display.blit(text_surface,(150+i*5,300+i*5))
                else:
                    for i in range(counter):
                        time.sleep(.09/counter)
                        self.display.blit(text_surface,(150+i*5,300+i*5))
                if(counter == 61):
                    self.starter_text = "10 Years"
                counter +=1
                #Create the text box class
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if(event.key == pygame.K_RETURN):
                            #Change to new room once built.
                            if(self.starter_text == "10 Years"):
                                self.starter_text = "I open the store, I buy the Hero's goods, I close the store, I cry "
                                self.result.remove("None")
                                self.result.append("entered")
                                self.gameStateManager.setCurrentState("exposition")                                
                                return
                pygame.display.flip()
                clock.tick(60)
        elif("firstMirror" == self.result[-1]):
            self.result.append("doneMirror")
            self.gameStateManager.setCurrentState("mirror")
        elif("firstShrine" == self.result[-1]):
            self.result.remove("firstShrine")
            self.gameStateManager.setCurrentState("shrine")
        elif("firstShop" == self.result[-1]):
            if("doneMirror" in self.result):                
                self.result.remove("firstShop")
                self.result.append("doneShop")
                self.gameStateManager.setCurrentState("storeExpo")
            else:
                text.textBox(self.display, 5, ["You Must Face Your Present Before Your Future"], pygame.font.SysFont("stixgeneralbolita", 24, bold=False, italic=False), self.gameStateManager).run() 
                self.gameStateManager.setCurrentState("firstPrompt")
        elif("doneShop" in self.result):
            self.gameStateManager.result.append(self.result[-1])
            self.gameStateManager.setCurrentState("guardExpo")
        elif("entered" in self.result):
            # print(self.result)
            #Set the state to a text input box.          
            self.gameStateManager.setCurrentState("firstPrompt")
        
            