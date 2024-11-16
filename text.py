import pygame
clock = pygame.time.Clock()
import os

class textBoxList():
    def __init__(self, display, speed, textFilename, next_room, font, gameState):
        self.textFilename = textFilename
        self.next_room = next_room
        self.display = display
        self.speed = speed
        self.font = font
        self.gameState = gameState
        self.text_lines = self.split_file()
        self.text_boxes = []
        self.create_list()
    
    def split_file(self):
        total_text = ""
        with open(self.textFilename, 'r') as text2:
            total_text = text2.readlines()
        return total_text
        
    def add(self, text):
        #create the textbox with the list of 1-3 lines. ending with the >
        text_box = textBox(self.display, self.speed, text, self.font, self.gameState)
        #Add the text box to the text box list.
        self.text_boxes.append(text_box)
    
    def create_list(self):
        if(os.path.getsize(self.textFilename) == 0):
            print("Error. No Text In File")
            return
        text = []
        for line in self.text_lines:
            line = line.strip()
            # print(line[-1])
            if(line == ""):
                continue
            text.append(line)
            if(line[-1] == ">"):
                self.add(text)
                text = []
    
    def run(self):
        #go through the lists textBox and then go to the last room.
        for textBox in self.text_boxes:
            textBox.run()
        self.gameState.setCurrentState(self.next_room)
        
    
        

class textBox():
    def __init__(self, display, speed, text, font, gameState):
        self.surface = display
        self.active_text = 0
        self.text = text
        self.texts = text[self.active_text]
        self.font = font
        self.speed = speed
        self.gameState = gameState
        self.text_in_progress = True
        self.counter = 0
        
        #Draw the text a bit at a time.
        
        
            #This then chains into the next text Box. maybe create a linked list class
            
    def run(self):
        Ongoing = True
        while(Ongoing):
            #This draws the black background and the white box.
            self.surface.fill((0,0,0))
            pygame.draw.rect(self.surface, "white", (0, 500, 600, 100), 2)
            if(self.text_in_progress):
                        current_text = self.font.render(self.texts[0:self.counter//self.speed], True, (255,255,255))
                        for i in range(self.active_text):
                                self.surface.blit(self.font.render(self.text[i], True, (255,255,255)),(10,510+(i*24)))
                        self.surface.blit(current_text, (10, 510+(self.active_text*24)))
                        self.counter += 1
            else:
                for i in range(len(self.text)):
                    self.surface.blit(self.font.render(self.text[i], True, (255,255,255)),(10,510+(i*24)))
            if(self.counter >= self.speed*len(self.texts)):
                    if(self.active_text+1 == len(self.text)):
                        self.text_in_progress = False
                    else:
                        self.active_text += 1
                        self.texts = self.text[self.active_text] 
                        self.counter = 0
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_RETURN):
                        if (self.text_in_progress == False):
                            Ongoing = False
                            self.counter = 0
                            self.active_text = 0
                            self.text_in_progress = True
                            self.texts = self.text[self.active_text]
                            return
                        if(self.active_text+1 == len(self.text)):
                            self.text_in_progress = False
                        else:
                            self.active_text += 1
                            self.texts = self.text[self.active_text]
                            self.counter = 0
                #Set up an if statement that checks if the enter key is pressed and all the words are written
                # if so it moves on to the room pointed next in the linked list
            pygame.display.flip()
            clock.tick(60)
        return
    
class textInput(textBox):
    def __init__(self, display, speed, text, font, gameState, room, returns) -> None:
         super().__init__(display, speed, text, font, gameState)
         #Add in the personal font of Alex. Since it's the same no matter what no need to pass it in.
         self.pFont = None
         self.userInput = ''
         self.room = room
         self.returns = returns
    
    def setRoom(self, room):
        self.room = room
    
    def run(self):
        #Draw the text imediately no scrolling. 
        #Then in a text box above the text box have them type their answer. 
        #send that answer back to the room. and then have that answer change the result attribute.
        Ongoing = True
        while(Ongoing):
            self.surface.fill((0,0,0))
            pygame.draw.rect(self.surface, "white", (0, 500, 600, 100), 2)
            pygame.draw.rect(self.surface, "white", (0, 450, 600, 50), 2)
            for i in range(len(self.text)):
                current_text = self.font.render(self.text[i], True, (255,255,255))        
                self.surface.blit(current_text, (10, 510+i*10))
            user_text = self.font.render(self.userInput, True, (255,255,255))
            self.surface.blit(user_text, (10, 460))
            for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        pygame.quit()
                    if(event.type == pygame.KEYDOWN):
                        if(event.key == pygame.K_BACKSPACE):
                            self.userInput = self.userInput[:-1]
                        elif(event.key == pygame.K_RETURN):
                            try:
                                self.room.result.append(self.returns[self.userInput])
                                self.userInput = ""
                                Ongoing = False
                                self.gameState.setCurrentState(self.room.name)
                                return 
                            except KeyError:
                                print("Not a provided answer")                         
                        else:
                            self.userInput += event.unicode            
            pygame.display.flip()
            clock.tick(60)
        return
        