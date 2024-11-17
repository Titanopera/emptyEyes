import PIL
import pygame
import button
import gsm
import room
from rooms import menu
from rooms import home
from rooms import cultist
import text
from rooms import mirror
from rooms import shrine
import npc
pygame.init()
clock = pygame.time.Clock()
skills = {"beg":1, "bluff":1, "blackmail":1}
alex = npc.alex(4, skills)

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#load button images
start_img = pygame.image.load("/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/images/start_btn.jpg").convert_alpha()
# load_img = pygame.image.load("images/load_btn.png").convert_alpha()
end_img = pygame.image.load("/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/images/end_btn.jpg").convert_alpha()
empty_eye_img = pygame.image.load("/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/images/empty_eye.jpg").convert_alpha() 
shrine_img1 = pygame.image.load("/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/images/shrine_img1.jpg").convert_alpha() 
shrine_img2 = pygame.image.load("/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/images/shrineImg2.jpg").convert_alpha() 
shrine_img3 = pygame.image.load("/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/images/shrineImg3.jpg").convert_alpha() 
bottle_img = pygame.image.load("/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/images/hedonism.jpg").convert_alpha() 
MMR_img = pygame.image.load("/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/images/mightMakesRight.jpg").convert_alpha() 
leader_img = pygame.image.load("/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/images/despairFreedom.jpg").convert_alpha() 
populist_img = pygame.image.load("/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/images/populist.jpg").convert_alpha() 
idea_img = pygame.image.load("/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/images/idealogue.jpg").convert_alpha() 

        
start_btn = button.Button(125, 375, start_img, (150, 60))
end_btn = button.Button(325, 375, end_img, (150, 60))
eye_btn = button.Button(100, 200, empty_eye_img, (400, 100))
mirror_btn = button.Button(100, 200, empty_eye_img, (400, 100))
shrine_btn1 = button.Button(100, 50, shrine_img1, (400, 500))
shrine_btn2 = button.Button(50, 25, shrine_img2, (200, 200))
shrine_btn3 = button.Button(250 ,300, shrine_img3, (200, 200))
bottle_btn = button.Button(200, 100, bottle_img, (200, 400))
MMR_btn = button.Button(200, 100, MMR_img, (100, 400))
populist_btn = button.Button(200, 100, populist_img, (100, 400))
idea_btn = button.Button(100, 100, idea_img, (300, 400))
leader_btn = button.Button(200, 100, leader_img, (100, 400))
        
#Create the game state and set it to menu
gameState = gsm.gameStateManager("menu")
old_base_font = pygame.font.Font(None, 24)
base_font = pygame.font.SysFont("stixgeneralbolita", 18, bold=False, italic=False)

states = {
    "home":home.Home(screen, 0, "None", gameState), 
    "menu":menu.Menu(screen, 0, {"eye_btn":eye_btn, "start_btn":start_btn, "end_btn":end_btn}, gameState), 
    "test1":text.textBox(screen, 5, ["Checking if this shit actually works", "Test For the second line", "Test For the third line. >"], base_font, gameState),
    "textBoxList":text.textBoxList(screen, 2, "/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/text_files/test1.txt", "menu", base_font, gameState),
    "exposition":text.textBoxList(screen, 2, "/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/text_files/expo.txt", "home", base_font, gameState),
    "firstPrompt":text.textInput(screen, 5, ["You find yourself in your home above your store front, you can move towards", "1. The Mirror Find Your Present", "2. The Shrine Find Your Past", "3.The Shop Find Your Future"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), gameState, "", {"1":"firstMirror", "2":"firstShrine", "3":"firstShop",}),
    "mirror":mirror.Mirror(screen, "None", {"mirror_btn":mirror_btn}, gameState, "", alex),
    "specChoose":text.textInput(screen, 5, ["Do You Wish To Specialize In", "1. Begging, see into others greatest desires, invoke pity, and persuade others", "2. Blackmail, see into others greatest fears, wield fear, and intimidate others", "3. Bluff, see what others want right now, wield lies, confuse others"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), gameState, "", {"1":"beg", "2":"blackmail", "3":"bluff",}),
    "shrine":shrine.Shrine(screen, "None", {"shrine_btn1":shrine_btn1, "shrine_btn2":shrine_btn2, "shrine_btn3":shrine_btn3}, gameState, ""),
    "storeExpo":text.textBoxList(screen, 2, "/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/text_files/storeExpo.txt", "store", pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), gameState),    
    "store":text.textInput(screen, 5, ["Before You Are Three Options", "1. A Knife, honed but fragile", "2. A Pull Stone, condensed wealth, will wealth help?", "3. Hat Of Disguise, a new face, it won't stick"], pygame.font.SysFont("stixgeneralbolita", 10, bold=False, italic=False), gameState, "", {"1":"knife", "2":"pStone", "3":"hatOD",}),
    "guardExpo":text.textBoxList(screen, 2, "/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/text_files/guardExpo.txt", "hedonist", pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), gameState),
    "hedonist":cultist.Hedonist(screen, "None", {"bottle_btn":bottle_btn, "eye_btn":eye_btn}, gameState),
    "storeExpo":text.textBoxList(screen, 2, "/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/text_files/storeExpo.txt", "store", pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), gameState),
    "idealogue":cultist.Idealogue(screen, "None", {"idea_btn":idea_btn, "eye_btn":eye_btn}, gameState),
    #Final boss not made yet.
    "fDrEeSePdAoImR":cultist.Leader(screen, "None", {"leader_btn":leader_btn, "eye_btn":eye_btn}, gameState),
    "epilogue":text.textBoxList(screen, 2, "/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/text_files/epi.txt", "store", pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), gameState),
}

#attaching the room to be changed here.
def setRoomFast(room, newRoom):
    states[room].setRoom(states[newRoom])

setRoomFast("firstPrompt", "home")
setRoomFast("mirror", "home")
setRoomFast("specChoose", "mirror")
setRoomFast("shrine", "home")
setRoomFast("store", "home")


play = True
while(play):
    try:
        states[gameState.getCurrentState()].run()
    except TypeError:
        states[gameState.getCurrentState()].run(alex)
    clock.tick(60)