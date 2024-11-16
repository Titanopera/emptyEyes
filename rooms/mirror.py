import pygame
import room
import npc
import text
clock = pygame.time.Clock()

class Mirror(room.Room):
    def __init__(self, display, result, objects, gameStateManager, homeRoom, alex) -> None:
        super().__init__(display, result, objects, gameStateManager)
        self.base_font = pygame.font.Font(None, 32)
        self.homeRoom = homeRoom
        self.name = "mirror"
        self.alex = alex
    
    def setRoom(self, newHomeRoom):
        self.homeRoom = newHomeRoom
        
    def run(self):
        if(self.result[-1]=="None"):
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                self.display.fill((0,0,0))
                if self.objects["mirror_btn"].draw(self.display):
                    #Move to the first room.
                    print("Mirror Clicked")
                    self.gameStateManager.setCurrentState("specChoose")
                    self.result.remove("None")
                    return
                pygame.display.flip()
                clock.tick(60)
        elif(self.result[-1]=="beg" or "bluff" or "blackmail"):
            if(self.result[-1]=="beg"):
                print("beg")
                skills = [3,2,1]
                self.result.remove("beg")
            elif(self.result[-1]=="bluff"):
                print("bluff")
                skills = [1,3,1]
                self.result.remove("bluff")
            elif(self.result[-1]=="blackmail"):    
                print("blackmail")
                skills = [1,2,3]
                self.result.remove("blackmail")            
            self.alex.redoSkills(skills)
            self.alex.printChar(self.display, self.gameStateManager, self.homeRoom)
            #Call the create alex thing.
        #catch all the new results and turn it into a thing. 
        # Then display the character sheet.
        #Then go back to home
        pass