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
            print(self.gameStateManager)
            for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        pygame.quit()
            if(self.result[-1]=="None"):
                self.display.fill((0,0,0))
                if self.objects["bottle_btn"].draw(self.display):
                    #Move to the first room.
                    print("Bottle Clicked")
                if self.objects["eye_btn"].draw(self.display):
                    print("Meeting of the Eyes Initiated Clicked")
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
                    text.textBox(self.display, 5, ["Jason", "No they have to care about me", "I've lost so much for them", "They're all I have left"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "They're not all you have left", "I'm here"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                if(self.result[-1] == "begFail" or self.result[-1] == "devLieFail"):
                    text.textBox(self.display, 5, ["The Hedonist", "Do you think I'm so pathetic that I would accept whatever scraps of love were tosed my way", "I'm a kind one for not smashing your head in right now"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "I deeply truly mean it Jason", "I'm here"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                if(self.result[-1] == "devLieSuccess"):
                    text.textBox(self.display, 5, ["The Hedonist", "No you haven't", "You can go past"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "Thank you Jason"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    self.gameStateManager.setCurrentState("idealogue")
                    return
                if(self.result[-1] == "devLieMixed"):
                    text.textBox(self.display, 5, ["The Hedonist", "*The Hedonist's face twisted into a frown he says*", "Yes, yes you have, you lied just now, why?", "*An uneasy expressions crosses his face, the Hedonist is unsure how to proceded*"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "I didn't lie Jason"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                if(self.result[-1] == "disguiseLieSuccess"):
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
                    text.textBox(self.display, 5, ["The Hedonist", "Eh you're right", "You can go past"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "Thank you Jason"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    self.gameStateManager.setCurrentState("idealogue")
                    return
                if(self.result[-1] == "bribeMixed"):
                    text.textBox(self.display, 5, ["The Hedonist", "I'm no rat I refuse your paltry bribe", "Keep the Pull Stone"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "*scowling a bit*", "Alright I'll accept that"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                if(self.result[-1] == "inspireJason"):
                    text.textBox(self.display, 5, ["Jason", "You're right, even if they were my friends it wouldn't matter if it meant helping them hurt Mary", "*Jason presses a gun he pulled out from somewhere into your hand and walks away*","You can go past"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "Thank you Jason"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    self.gameStateManager.setCurrentState("idealogue")
                    return
                if(self.result[-1] == "lieHelpSuccess"):
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
                    alex.useBeg()
                    self.gameStateManager.result.append("inspireHedonist")
                if(alex.skills["beg"] < 1):
                    dialogue.append("1. Jason what are you doing here, do you really think these people are your friends if you're standing gaurd outside barely wearing a thing")
                    answers["1"] = "begFail"
                    alex.useBeg()
                if(alex.skills["bluff"] <= 1):
                    dialogue.append("2. (Lie) Jason I care about you")
                    alex.useBluff()
                    answers["2"] = "devLieFail"
                if(alex.skills["bluff"] > 1):
                    alex.useBluff()
                    dialogue.append("2. (Lie) Jason what are you doing here, do you really think these people are your friends if you're standing gaurd outside barely wearing a thing")
                    answers["2"] = "lieSuccess"
                if(alex.skills["bluff"] >= 3 and "lieSuccess" in self.result):
                    alex.useBluff()
                    dialogue.append("3. (Lie) You know me Jason, have I ever lied to you let me pass")
                    answers["3"] = "devLieSucess"
                    self.gameStateManager.result.append("devastatingLieHedonist")
                if(alex.skills["bluff"] < 3 and "lieSuccess" in self.result):
                    alex.useBluff()
                    dialogue.append("3. (Lie) You know me Jason, have I ever lied to you let me pass")
                    answers["3"] = "devLieMixed"
                if("hatOD" in self.gameStateManager.result):
                    alex.useBluff()
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
                    alex.useBlackmail()
                if("pStone" in self.gameStateManager.result and alex.skills["beg"] >=5):
                    alex.useBeg()
                    dialogue.append("6. (Pull Stone) You could buy a lot of alchohol with this Jason")
                    self.gameStateManager.result.remove("pStone")
                    answers["6"] = "bribeSuccess"
                    self.gameStateManager.result.append("furtherAddictionHedonist")
                elif("pStone" in self.gameStateManager.result and alex.skills["beg"] >=3):
                    alex.useBeg()
                    dialogue.append("6. (Pull Stone) If I give you this Pull Stone will you let me slip past")
                    answers["6"] = "bribeMixed"
                elif("pStone" in self.gameStateManager.result and alex.skills["beg"] < 3):
                    alex.useBeg()
                    dialogue.append("6. (Pull Stone) If I give you this Pull Stone will you let me slip past")
                    answers["6"] = "bribeFail"
                if("begSuccess" in self.result or alex.skills["beg"] >=5):
                    alex.useBeg()
                    dialogue.append("7. You matter Jason, and if you help me, you can finally be someone you can be proud of")
                    answers["7"] = "inspireJason"
                    self.gameStateManager.result.append("gun")
                    self.gameStateManager.result.append("inspireHedonist")
                if(alex.skills["bluff"] >=5):
                    alex.useBluff()
                    dialogue.append("8. Jason, I'm one important motherfucker and if you help me, I'll make sure the big guy knows you helped me out")
                    answers["8"] = "lieHelpJason"
                    self.gameStateManager.result.append("alchohol")
                    self.gameStateManager.result.append("harmlessLieHedonist")
                if(alex.skills["blackmail"] >=5 or "devLieSuccess" in self.result or "devLieMixed" in self.result):
                    alex.useBlackmail()
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
            print(self.gameStateManager)
            for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        pygame.quit()
            if(self.result[-1]=="None"):
                self.display.fill((0,0,0))
                if self.objects["idea_btn"].draw(self.display):
                    #Move to the first room.
                    print("Mask Clicked")
                if self.objects["eye_btn"].draw(self.display):
                    print("Meeting of the Eyes Initiated Clicked")
                    self.result.append("MotE")
            elif("MotE" in self.result):
                print(self.gameStateManager)
                #Pop up a text.textBoxList here on the first go around.
                if(self.counter == 0):
                    hedExpo = text.textBoxList(self.display, 2, "/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/text_files/ideaExpo.txt", "idealogue", pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager)
                    hedExpo.run()
                if(self.counter > 3):
                    #textBox here then quit
                    text.textBox(self.display, 5, ["In A Flash", "You Die, Your Head Flying Off In An Instant", "In Your Last Moments You're Not Sure If You Regretted This"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    sys.quit()
                #Set up a bunch of dialogue checks to see what Jason says.
                print(self.result)
                if(self.result[-1] == "begSuccess" or self.result[-1] == "lieSuccess"):
                    text.textBox(self.display, 5, ["Jason", "No they have to care about me", "I've lost so much for them", "They're all I have left"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "They're not all you have left", "I'm here"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                if(self.result[-1] == "begFail" or self.result[-1] == "devLieFail"):
                    text.textBox(self.display, 5, ["The Hedonist", "Do you think I'm so pathetic that I would accept whatever scraps of love were tosed my way", "I'm a kind one for not smashing your head in right now"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "I deeply truly mean it Jason", "I'm here"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                if(self.result[-1] == "devLieSuccess"):
                    text.textBox(self.display, 5, ["The Hedonist", "No you haven't", "You can go past"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "Thank you Jason"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    self.gameStateManager.setCurrentState("idealogue")
                    return
                if(self.result[-1] == "devLieMixed"):
                    text.textBox(self.display, 5, ["The Hedonist", "*The Hedonist's face twisted into a frown he says*", "Yes, yes you have, you lied just now, why?", "*An uneasy expressions crosses his face, the Hedonist is unsure how to proceded*"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "I didn't lie Jason"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                if(self.result[-1] == "disguiseLieSuccess"):
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
                    text.textBox(self.display, 5, ["The Hedonist", "Eh you're right", "You can go past"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "Thank you Jason"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    self.gameStateManager.setCurrentState("idealogue")
                    return
                if(self.result[-1] == "bribeMixed"):
                    text.textBox(self.display, 5, ["The Hedonist", "I'm no rat I refuse your paltry bribe", "Keep the Pull Stone"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "*scowling a bit*", "Alright I'll accept that"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                if(self.result[-1] == "inspireJason"):
                    text.textBox(self.display, 5, ["Jason", "You're right, even if they were my friends it wouldn't matter if it meant helping them hurt Mary", "*Jason presses a gun he pulled out from somewhere into your hand and walks away*","You can go past"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    text.textBox(self.display, 5, ["Alex", "Thank you Jason"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), self.gameStateManager).run()
                    self.gameStateManager.setCurrentState("idealogue")
                    return
                if(self.result[-1] == "lieHelpSuccess"):
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
                    alex.useBeg()
                    self.gameStateManager.result.append("inspireHedonist")
                if(alex.skills["beg"] < 1):
                    dialogue.append("1. Jason what are you doing here, do you really think these people are your friends if you're standing gaurd outside barely wearing a thing")
                    answers["1"] = "begFail"
                    alex.useBeg()
                if(alex.skills["bluff"] <= 1):
                    dialogue.append("2. (Lie) Jason I care about you")
                    alex.useBluff()
                    answers["2"] = "devLieFail"
                if(alex.skills["bluff"] > 1):
                    alex.useBluff()
                    dialogue.append("2. (Lie) Jason what are you doing here, do you really think these people are your friends if you're standing gaurd outside barely wearing a thing")
                    answers["2"] = "lieSuccess"
                if(alex.skills["bluff"] >= 3 and "lieSuccess" in self.result):
                    alex.useBluff()
                    dialogue.append("3. (Lie) You know me Jason, have I ever lied to you let me pass")
                    answers["3"] = "devLieSucess"
                    self.gameStateManager.result.append("devastatingLieHedonist")
                if(alex.skills["bluff"] < 3 and "lieSuccess" in self.result):
                    alex.useBluff()
                    dialogue.append("3. (Lie) You know me Jason, have I ever lied to you let me pass")
                    answers["3"] = "devLieMixed"
                if("hatOD" in self.gameStateManager.result):
                    alex.useBluff()
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
                    alex.useBlackmail()
                if("pStone" in self.gameStateManager.result and alex.skills["beg"] >=5):
                    alex.useBeg()
                    dialogue.append("6. (Pull Stone) You could buy a lot of alchohol with this Jason")
                    self.gameStateManager.result.remove("pStone")
                    answers["6"] = "bribeSuccess"
                    self.gameStateManager.result.append("furtherAddictionHedonist")
                elif("pStone" in self.gameStateManager.result and alex.skills["beg"] >=3):
                    alex.useBeg()
                    dialogue.append("6. (Pull Stone) If I give you this Pull Stone will you let me slip past")
                    answers["6"] = "bribeMixed"
                elif("pStone" in self.gameStateManager.result and alex.skills["beg"] < 3):
                    alex.useBeg()
                    dialogue.append("6. (Pull Stone) If I give you this Pull Stone will you let me slip past")
                    answers["6"] = "bribeFail"
                if("begSuccess" in self.result or alex.skills["beg"] >=5):
                    alex.useBeg()
                    dialogue.append("7. You matter Jason, and if you help me, you can finally be someone you can be proud of")
                    answers["7"] = "inspireJason"
                    self.gameStateManager.result.append("gun")
                    self.gameStateManager.result.append("inspireHedonist")
                if(alex.skills["bluff"] >=5):
                    alex.useBluff()
                    dialogue.append("8. Jason, I'm one important motherfucker and if you help me, I'll make sure the big guy knows you helped me out")
                    answers["8"] = "lieHelpJason"
                    self.gameStateManager.result.append("alchohol")
                    self.gameStateManager.result.append("harmlessLieHedonist")
                if(alex.skills["blackmail"] >=5 or "devLieSuccess" in self.result or "devLieMixed" in self.result):
                    alex.useBlackmail()
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