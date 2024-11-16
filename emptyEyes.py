import PIL
import pygame
import button
import gsm
import room
from rooms import menu
from rooms import home
import text
import ottterJams.November_2024_UnseenWorlds.rooms.mirror as mirror
pygame.init()
clock = pygame.time.Clock()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#load button images
start_img = pygame.image.load("/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/images/start_btn.jpg").convert_alpha()
# load_img = pygame.image.load("images/load_btn.png").convert_alpha()
end_img = pygame.image.load("/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/images/end_btn.jpg").convert_alpha()
empty_eye_img = pygame.image.load("/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/images/empty_eye.jpg").convert_alpha() 
        
start_btn = button.Button(125, 375, start_img, (150, 60))
end_btn = button.Button(325, 375, end_img, (150, 60))
eye_btn = button.Button(100, 200, empty_eye_img, (400, 100))
mirror_btn = button.Button(100, 200, empty_eye_img, (400, 100))
        
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
    "mirror":mirror.Mirror(screen, "None", {"mirror_btn":mirror_btn}, gameState, ""),
    "specChoose":text.textInput(screen, 5, ["Do You Wish To Specialize In", "1. Begging, see into others greatest desires, invoke pity, and persuade others", "2. Blackmail, see into others greatest fears, wield fear, and intimidate others", "3. Bluff, see what others want right now, wield lies, confuse others"], pygame.font.SysFont("stixgeneralbolita", 12, bold=False, italic=False), gameState, "", {"1":"beg", "2":"blackmail", "3":"bluff",}),
}

#attaching the room to be changed here.
def setRoomFast(room, newRoom):
    states[room].setRoom(states[newRoom])

setRoomFast("firstPrompt", "home")
setRoomFast("mirror", "home")
setRoomFast("specChoose", "mirror")

play = True
while(play):
    states[gameState.getCurrentState()].run()
    clock.tick(60)