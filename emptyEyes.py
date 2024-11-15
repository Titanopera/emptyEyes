import PIL
import pygame
import button
import gsm
import room
from rooms import menu
from rooms import home
import text
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
        
#Create the game state and set it to menu
gameState = gsm.gameStateManager("menu")
old_base_font = pygame.font.Font(None, 24)
base_font = pygame.font.SysFont("stixgeneralbolita", 18, bold=False, italic=False)

states = {
    "home":home.Home(screen, 0, "null", gameState), 
    "menu":menu.Menu(screen, 0, {"eye_btn":eye_btn, "start_btn":start_btn, "end_btn":end_btn}, gameState), 
    "test1":text.textBox(screen, 5, ["Checking if this shit actually works", "Test For the second line", "Test For the third line. >"], base_font, gameState),
    "textBoxList":text.textBoxList(screen, 2, "/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/text_files/test1.txt", "menu", base_font, gameState),
    "exposition":text.textBoxList(screen, 2, "/Users/alexey/Desktop/visualStudioPrograms/ottterJams/November_2024_UnseenWorlds/text_files/expo.txt", "menu", base_font, gameState),
}

play = True
while(play):
    states[gameState.getCurrentState()].run()
    clock.tick(60)