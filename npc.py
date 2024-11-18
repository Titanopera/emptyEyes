import sys
import text
import pygame
class Alex():
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
        
        gameState.setCurrentState(homeRoom)
        
    def redoSkills(self, skills):
        self.skills["beg"] = skills[0]
        self.skills["bluff"] = skills[1]
        self.skills["blackmail"] = skills[2]
        
    def useBeg(self):
        print(self.skills)
        self.skills["beg"] = self.skills["beg"] + 3
        self.skills["bluff"] = self.skills["bluff"] -1
        self.skills["blackmail"] = self.skills["blackmail"]-1
        if(self.skills["beg"] > 10):
            self.skills["beg"] = 10
        if(self.skills["bluff"] <= 0):
            self.skills["bluff"] = 0
        if(self.skills["blackmail"] <= 0):
            self.skills["blackmail"] = 0
        print(self.skills)
        
            
    def useBluff(self):
        print(self.skills)
        self.skills["beg"] = self.skills["beg"] - 1
        self.skills["bluff"] = self.skills["bluff"] + 3
        self.skills["blackmail"] -= self.skills["blackmail"]-1
        if(self.skills["bluff"] > 10):
            self.skills["bluff"] = 10
        if(self.skills["beg"] <= 0):
            self.skills["beg"] = 0
        if(self.skills["blackmail"] <= 0):
            self.skills["blackmail"] = 0
        print(self.skills)
        
            
    def useBlackmail(self):
        print(self.skills)
        self.skills["beg"] -= self.skills["beg"] - 1
        self.skills["bluff"] = self.skills["bluff"]- 1
        self.skills["blackmail"] = self.skills["blackmail"]+3
        if(self.skills["blackmail"] > 10):
            self.skills["blackail"] = 10
        if(self.skills["bluff"] <=0):
            self.skills["bluff"] = 0
        if(self.skills["beg"] <=0):
            self.skills["beg"] = 0
        print(self.skills)
            
        
        
        