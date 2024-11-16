import sys
import text
import pygame
class alex():
    def __init__(self, hp, skills):
        self.hp = hp
        self.skills = skills
        
    def printChar(self, screen, gameState, homeRoom):
        #Do this in the text box.
        texts = []
        texts.append("Name: Alex")
        texts.append("Beg: " + str(self.skills["beg"]))
        texts.append("Bluff: " + str(self.skills["bluff"]))
        texts.append("Blackmail: " + str(self.skills["blackmail"]))
        # smaller font size and it would be the custom font.
        text.textBox(screen, 5, texts, pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), gameState).run() 
        
        gameState.setCurrentState(homeRoom.name)
        
            
    
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
        
        
        