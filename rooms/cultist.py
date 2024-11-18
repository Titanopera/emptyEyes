import pygame
import room
import text
import sys
clock = pygame.time.Clock()

class Hedonist(room.Room):
    def __init__(self, display, objects, gameStateManager, result) -> None:
        super().__init__(display, objects, gameStateManager, result)
        self.base_font = pygame.font.Font(None, 32)
        self.counter = 0
        self.name = "hedonist"
        
    def run(self, alex):
        while(True):
            print(alex.skills)
            for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        pygame.quit()
            if(self.result[-1]=="None"):
                self.display.fill((0,0,0))
                if self.objects["bottle_btn"].draw(self.display):
                    #Move to the first room.
                    print("Bottle Clicked")
                    print("Meeting of the Eyes Initiated")
                    self.result.append("MotE")
            elif("MotE" in self.result):
                print(self.gameStateManager)
                #Pop up a text.textBoxList here on the first go around.
                if(self.counter == 0):
                    hedExpo = text.textBoxList(self.display, 2, "/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/text_files/hedExpo.txt", "hedonist", pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager)
                    hedExpo.run()
                if(self.counter > 3):
                    #textBox here then quit
                    text.textBox(self.display, 5, ["In A Flash", "You Die, Your Head Smashed Open By A Bottle Of Whiskey", "In Your Last Moments You're Not Sure If You Regretted This"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    sys.quit()
                #Set up a bunch of dialogue checks to see what Jason says.
                print(self.result)
                if(self.result[-1] == "begSuccess" or self.result[-1] == "lieSuccess"):
                    alex.useBeg()
                    text.textBox(self.display, 5, ["Jason", "No they have to care about me", "I've lost so much for them", "They're all I have left"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "They're not all you have left", "I'm here"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                if(self.result[-1] == "begFail" or self.result[-1] == "devLieFail"):
                    text.textBox(self.display, 5, ["The Hedonist", "Do you think I'm so pathetic that I would accept whatever scraps of love were tosed my way", "I'm a kind one for not smashing your head in right now"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "I deeply truly mean it Jason", "I'm here"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                if(self.result[-1] == "devLieSuccess"):
                    alex.useBluff()
                    text.textBox(self.display, 5, ["The Hedonist", "No you haven't", "You can go past"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "Thank you Jason"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    self.gameStateManager.setCurrentState("idealogue")
                    return
                if(self.result[-1] == "devLieMixed"):
                    alex.useBluff()
                    text.textBox(self.display, 5, ["The Hedonist", "*The Hedonist's face twisted into a frown he says*", "Yes, yes you have, you lied just now, why?", "*An uneasy expressions crosses his face, the Hedonist is unsure how to proceded*"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "I didn't lie Jason"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                if(self.result[-1] == "disguiseLieSuccess"):
                    alex.useBluff()
                    text.textBox(self.display, 5, ["The Hedonist", "Of Course Sir", "*Jason hastily moves aside a couple bottles*","You can go past"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "Thank you Jason"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    self.gameStateManager.setCurrentState("idealogue")
                    return
                if(self.result[-1] == "killHedonist"):
                    text.textBox(self.display, 5, ["The Hedonist", "*In a moment of distraction you sink the obsidian knife into The Hedonist*", "*It writhes in pain, as the obsidian shatters inside its body*","*It stares back up at you confused, as it bleeds out and dies*"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "*I breathe in and out, my stomach heaving as I stare at the corpse*", "Unable to take it any longer the contents of my stomach spew on the floor, some bits splattering over the corpse", "I wipe my mouth of the bile before stepping over it and moving on"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    self.gameStateManager.setCurrentState("idealogue")
                    return
                if(self.result[-1] == "failBlackmail" or self.result[-1] == "failBribe"):
                    text.textBox(self.display, 5, ["The Hedonist", "*The Hedonist's face twists into a horrifying scowl", "Do you think I am a rat, one to scurry around for your whims", "*The Hedonist approaches you a bottle in his hand*"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "I raise my hands over my head as I scream","No Please Wait"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["In A Flash", "You Die, Your Head Smashed Open By A Bottle Of Whiskey", "In Your Last Moments You're Not Sure If You Regretted This"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    sys.quit()
                if(self.result[-1] == "bribeSuccess"):
                    alex.useBeg()
                    self.gameStateManager.result.remove("pStone")                    
                    text.textBox(self.display, 5, ["The Hedonist", "Eh you're right", "You can go past"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "Thank you Jason"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    self.gameStateManager.setCurrentState("idealogue")
                    return
                if(self.result[-1] == "bribeMixed"):
                    alex.useBeg()                    
                    text.textBox(self.display, 5, ["The Hedonist", "I'm no rat I refuse your paltry bribe", "Keep the Pull Stone"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "*scowling a bit*", "Alright I'll accept that"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                if(self.result[-1] == "inspireJason"):
                    alex.useBeg()
                    text.textBox(self.display, 5, ["Jason", "You're right, even if they were my friends it wouldn't matter if it meant helping them hurt Mary", "*Jason presses a gun he pulled out from somewhere into your hand and walks away*","You can go past"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "Thank you Jason"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    self.gameStateManager.setCurrentState("idealogue")
                    return
                if(self.result[-1] == "lieHelpSuccess"):
                    alex.useBluff()                    
                    text.textBox(self.display, 5, ["The Hedonist", "Huh didn't know you were that important", "*Jason hastily moves aside a couple bottles*","You can go past"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["The Hedonist", "Hell have a bottle from me", "*Jason hastily moves grabs one of the rare full bottles and hands it to you*"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "Thank you Jason", "I'll put in a good word for you"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    self.gameStateManager.setCurrentState("idealogue")
                    return
                if(self.result[-1] == "destroyJason"):                    
                    text.textBox(self.display, 5, ["Jason", "*Jason's face twists into a horrific grimace*", "Jason on the floor babbles, No, No, No, I'm not worthless"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["As a gun clatters to the floor you pick it up", "Then with a casual jaunt you step over Jason's comatose body"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    self.gameStateManager.setCurrentState("idealogue")
                    return
                #From here have a loop of checks that figure out what dialogue options there are then initiate a prompt
                answers = {}
                dialogue = []
                if(alex.skills["beg"] >= 1):
                    dialogue.append("1. Jason what are you doing here, do you really think these people are your friends if you're standing gaurd outside barely wearing a thing")
                    answers["1"] = "begSuccess"
                    self.gameStateManager.result.append("inspireHedonist")
                if(alex.skills["beg"] < 1):
                    dialogue.append("1. Jason what are you doing here, do you really think these people are your friends if you're standing gaurd outside barely wearing a thing")
                    answers["1"] = "begFail"                    
                if(alex.skills["bluff"] >= 1):
                    dialogue.append("2. (Lie) Jason I care about you")
                    answers["2"] = "lieSuccess"
                elif(alex.skills["bluff"] < 1):                    
                    dialogue.append("2. (Lie) Jason what are you doing here, do you really think these people are your friends if you're standing gaurd outside barely wearing a thing")
                    answers["2"] = "lieSuccess"
                if(alex.skills["bluff"] >= 3 and "lieSuccess" in self.result):                    
                    dialogue.append("3. (Lie) You know me Jason, have I ever lied to you let me pass")
                    answers["3"] = "devLieSucess"
                    self.gameStateManager.result.append("devastatingLieHedonist")
                if(alex.skills["bluff"] < 3 and "lieSuccess" in self.result):                    
                    dialogue.append("3. (Lie) You know me Jason, have I ever lied to you let me pass")
                    answers["3"] = "devLieMixed"
                if("hatOD" in self.gameStateManager.result):                    
                    dialogue.append("4. (Hat Of Disguise) *Transform into Cultist* May I come in?")
                    answers["4"] = "disguiseLieSuccess"
                    self.gameStateManager.result.append("harmlessLieHedonist")
                if("knife" in self.gameStateManager.result and ("distracted" in self.result or "devLieMixed")):
                    dialogue.append("5. (Knife) While The Hedonist is distracted, you stab him in the back")
                    answers["5"] = "killHedonist"
                    self.gameStateManager.result.append("killedHedonist")
                elif("knife" in self.gameStateManager.result):
                    dialogue.append("5. (Knife) You threaten The Hedonist with the Knife")
                    answers["5"] = "failBlackmail"                    
                if("pStone" in self.gameStateManager.result and alex.skills["beg"] >=5):                    
                    dialogue.append("6. (Pull Stone) You could buy a lot of alchohol with this Jason")                    
                    answers["6"] = "bribeSuccess"
                    self.gameStateManager.result.append("furtherAddictionHedonist")
                elif("pStone" in self.gameStateManager.result and alex.skills["beg"] >=3):                    
                    dialogue.append("6. (Pull Stone) If I give you this Pull Stone will you let me slip past")
                    answers["6"] = "bribeMixed"
                elif("pStone" in self.gameStateManager.result and alex.skills["beg"] < 3):                    
                    dialogue.append("6. (Pull Stone) If I give you this Pull Stone will you let me slip past")
                    answers["6"] = "bribeFail"
                if("begSuccess" in self.result or alex.skills["beg"] >=5):                    
                    dialogue.append("7. You matter Jason, and if you help me, you can finally be someone you can be proud of")
                    answers["7"] = "inspireJason"
                    self.gameStateManager.result.append("gun")
                    self.gameStateManager.result.append("inspireHedonist")
                if(alex.skills["bluff"] >= 5):                    
                    dialogue.append("8. Jason, I'm one important motherfucker and if you help me, I'll make sure the big guy knows you helped me out")
                    answers["8"] = "lieHelpSuccess"
                    self.gameStateManager.result.append("alchohol")
                    self.gameStateManager.result.append("harmlessLieHedonist")
                if(alex.skills["blackmail"] >=5 or "devLieSuccess" in self.result or "devLieMixed" in self.result):                    
                    dialogue.append("9. Jason, Jason, Jason did you really believe me when I said we were friends? You don't have any friends, you're a worthless drunk idiot")
                    answers["9"] = "destroyJason"
                    self.gameStateManager.result.append("gun")
                    self.gameStateManager.result.append("devastateHedonist")
                
                #Run
                print(self.result)
                check = text.textInput(self.display, 5, dialogue, pygame.font.SysFont("stixgeneralbolita", 10, bold=False, italic=False), self.gameStateManager, self, answers)
                check.run()
                #After the prompt is done, increment by one 
                print(self.counter)
                self.counter += 1
            pygame.display.flip()
            clock.tick(60)
            

class Idealogue(room.Room):
    def __init__(self, display, objects, gameStateManager, result) -> None:
        super().__init__(display, objects, gameStateManager, result)
        self.base_font = pygame.font.Font(None, 32)
        self.counter = 0
        self.name = "idealogue"
        
    def run(self, alex):
        while(True):
            print(self.gameStateManager.result)
            for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        pygame.quit()
            if(self.result[-1]=="None"):
                if(self.counter == 0):
                    hedExpo = text.textBoxList(self.display, 2, "/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/text_files/ideaExpo.txt", "idealogue", pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager)
                    hedExpo.run()
                    self.counter += 1 
                self.display.fill((0,0,0))
                if self.objects["idea_btn"].draw(self.display):
                    #Move to the first room.
                    print("Mask Clicked")
                    print("Meeting of the Eyes Initiated")
                    self.result.append("MotE")
                    self.counter = 0
            elif("MotE" in self.result):
                print(self.gameStateManager)                    
                if(self.counter > 3):
                    #textBox here then quit
                    text.textBox(self.display, 5, ["In A Flash", "You Die, Your Head Flying Off In An Instant", "In Your Last Moments You're Not Sure If You Regretted This"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    pygame.quit()
                #Set up a bunch of dialogue checks to see what Jason says.
                print(self.result)
                if(self.result[-1] == "question"):
                    alex.useBeg()
                    text.textBox(self.display, 5, ["The Idealogue", "Because fDrEeSePdAoImR is greather than I", "I can entrust the truth to them", "I am one amongst many, who have each found the truth through their eyes"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()                    
                if(self.result[-1] == "blackSuccess"):
                    alex.useBlackmail()
                    text.textBox(self.display, 5, ["The Idealogue", "They would never do such a thing to me their most valued servant", "*An Involuntary shivver rings through them*"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                if(self.result[-1] == "askLeader"):
                    alex.useBeg()
                    alex.useBluff()
                    text.textBox(self.display, 5, ["The Idealogue", "Hmm that makes sense I'll consult with them"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                if(self.result[-1] == "disguiseSuccess"):
                    alex.useBluff()
                    text.textBox(self.display, 5, ["The Idealogue", "*They look at you and scrunch their eyes underneath their blindfold*", "Who are you again?"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "I'm a new recruit", "I just saw someone sneak away while you weren't looking", "So"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["The Idealogue", "*An alarmed expression flashes across their blank face*", "Oh, oh no. If they were running they really were an intruder", "*They stride off looking quite alarmed*"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()                    
                    self.gameStateManager.setCurrentState("fDrEeSePdAoImR")
                    return
                if(self.result[-1] == "failAskLeader"):
                    text.textBox(self.display, 5, ["The Idealogue", "*Their empty eyes twitch* No my word is his will miscreant", "Be Still And SILENT!", "With a shing a previously unseen swords lops your head off"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    pygame.quit()
                if(self.result[-1] == "bribeSuccess"):
                    alex.useBeg()
                    text.textBox(self.display, 5, ["The Idealogue", "*Briefly a conflicted look pops up on their blank face before they wipe it away*", "This could be quite useful", "Alright I won't bother you, it's not like you'll succeed anyway."], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    self.gameStateManager.setCurrentState("fDrEeSePdAoImR")
                    return
                if(self.result[-1] == "killIdealogue"):
                    text.textBox(self.display, 5, ["The Idealogue", "One moment they stare at you smugly the next, with a clatter and a series of bangs, they're on the floor dead", "It seems too small for such a larger than life figure, now they're nothing more than a bleeding pile of flesh"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    if("killedHedonist" in self.gameStateManager.result):
                        text.textBox(self.display, 5, ["Alex", "Oh Above and Below she was frightening" "*I pick up the sword that clattered to the ground*"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    else:
                        text.textBox(self.display, 5, ["Alex", "*I breathe in and out, my stomach heaving as I stare at the corpse*", "Unable to take it any longer the contents of my stomach spew on the floor, some bits splattering over the corpse", "I wipe my mouth of the bile before stepping over it and moving on"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    self.gameStateManager.setCurrentState("fDrEeSePdAoImR")
                    return
                if(self.result[-1] == "freeJanice"):                    
                    text.textBox(self.display, 5, ["Janice", "*Jason's face twists into a horrific grimace*", "Jason on the floor babbles, No, No, No, I'm not worthless"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["As a gun clatters to the floor you pick it up", "Then with a casual jaunt you step over Jason's comatose body"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    self.gameStateManager.setCurrentState("fDrEeSePdAoImR")
                    return
                #From here have a loop of checks that figure out what dialogue options there are then initiate a prompt
                answers = {}
                dialogue = []
                if(alex.skills["beg"] > 1):
                    dialogue.append("1. If life has no meaning then how can they give it meaning, if you can't?")
                    answers["1"] = "question"                    
                if(alex.skills["blackmail"] >= 1 and "question" in self.result):
                    dialogue.append("2. If you're just one amongst many aren't you disposable")                    
                    answers["2"] = "blackSuccess"
                if(alex.skills["beg"] >= 5):                    
                    dialogue.append("3. Wait, wait, before you do anything shouldn't you check with the leader first")
                    answers["3"] = "askLeader"                    
                elif(alex.skills["bluff"] >= 3):                    
                    dialogue.append("3. Hey hey I'm not some ordinary bloke, I'm in the middle of the caves shouldn't you get prior authorization first")
                    answers["3"] = "askLeader"
                elif(alex.skills["beg"] < 5 and alex.skills["bluff"] < 3):
                    dialogue.append("3. If you are such a nincompoop that you can't even think of your own philosophy then shouldn't you ask")
                    answers["3"] = "failAskLeader"
                if("pStone" in self.gameStateManager.result or "alchohol" in self.gameStateManager.result):                    
                    dialogue.append("4. (Pull Stone/Alchohol) You look like someone who's been searching for a gift, I wonder if this would work for you")
                    answers["4"] = "bribeSuccess"
                    self.gameStateManager.result.append("bribeIdealogue")
                if("gun" in self.gameStateManager.result):
                    dialogue.append("5. (Gun) You pull the trigger of the gun and keep pulling until they're dead")
                    answers["5"] = "killIdealogue"
                    self.gameStateManager.result.append("killedIdealogue")
                if("hatOD" in self.gameStateManager.result and "askLeader" in self.result):                    
                    dialogue.append("6. (Hat Of Disguise) While the Idealogue was turned around going off to ask their leader for advice you put on a disguise and snuck off")
                    self.gameStateManager.result.remove("hatOD")
                    answers["6"] = "disguiseSuccess"
                    self.gameStateManager.result.append("spareHedonist")
                if("blackSuccess" in self.result and alex.skills["blackmail"] >=3):                    
                    dialogue.append("7. Is a minion that understands that it's disposable a good minion, what would happen if I were to tell your boss")
                    answers["7"] = "disheartenJanice"
                    self.gameStateManager.result.append("disheartenIdealogue")
                elif("blackSuccess" in self.result and not alex.skills["blackmail"] >= 3):                    
                    dialogue.append("7. Is a minion that understands that it's disposable a good minion, what would happen if I were to tell your boss")
                    answers["7"] = "failDisheartenJanice"
                if(alex.skills["bluff"] >=5):                    
                    dialogue.append("8. What you've said makes so much sense, I think I'm going to convert?")
                    answers["8"] = "lieSurrender"
                    self.gameStateManager.result.append("harmlessLieIdealogue")
                if(alex.skills["beg"] >=7 and "blackSuccess" in self.result):                    
                    dialogue.append("9. If you're so worthless to him, and to be discarded so easily then why do you follow him")
                    answers["9"] = "freeJanice"
                    self.gameStateManager.result.append("sword")
                    self.gameStateManager.result.append("freeJanice")
                
                #Run
                print(self.result)
                check = text.textInput(self.display, 5, dialogue, pygame.font.SysFont("stixgeneralbolita", 10, bold=False, italic=False), self.gameStateManager, self, answers)
                check.run()
                #After the prompt is done, increment by one 
                print(self.counter)
                self.counter += 1
            pygame.display.flip()
            clock.tick(60)
            
class Leader(room.Room):
    def __init__(self, display, objects, gameStateManager, result) -> None:
        super().__init__(display, objects, gameStateManager, result)
        self.base_font = pygame.font.Font(None, 32)
        self.counter = 0
        
    def run(self, alex):
        while(True):
            for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        pygame.quit()
            self.display.fill((0,0,0))
            if self.objects["leader_btn"].draw(self.display):
                self.gameStateManager.setCurrentState("epilogue")
            pygame.display.flip()
            clock.tick(60)
            
                