import sys
import text
class alex():
    def __init__(self, hp, stats, skills):
        self.hp = hp
        self.stats = stats
        self.skills = skills
        
    def printChar(self, gameState, homeRoom):
        #Do this in the text box.
        text = []
        text.append("Name: Alex")
        print("Hp: " + str(self.hp))
        for key, value in self.stats.items():
            text.append(str(key) + ": " + str(value))
        for key, value in self.skills.values():
            text.append(str(key) + ": " + str(value))
        # smaller font size and it would be the custom font.
        text.textBox()
        #Start a textbox here. 
        
        gameState.setCurrent(homeRoom)
        
            
    
    def increaseSkill(self, skill):
        self.skills[skill] += 1
    
    def increaseStat(self, skill):
        self.stats[skill] += 1
    
    def lowerHp(self, damgae):
        hp -= damgae
        if(hp <= 0):
            #Print a death thing.
            sys.quit()
class npc():
    def __init__(self, hp, stats, skills):
        self.hp = hp
        self.stats = stats
        self.skills = skills
        
        
        