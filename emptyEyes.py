import PIL
import pygame
import button
import gsm
import room
from rooms import menu
from rooms import home

pygame.init()
clock = pygame.time.Clock()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#load button images
start_img = pygame.image.load("images/start_btn.jpg").convert_alpha()
# load_img = pygame.image.load("images/load_btn.png").convert_alpha()
end_img = pygame.image.load("images/end_btn.jpg").convert_alpha()
empty_eye_img = pygame.image.load("images/empty_eye.jpg").convert_alpha() 
        
start_btn = button.Button(125, 375, start_img, (150, 60))
end_btn = button.Button(325, 375, end_img, (150, 60))
eye_btn = button.Button(100, 200, empty_eye_img, (400, 100))
        
#Create the game state and set it to menu
gameState = gsm.gameStateManager("menu")

states = {"home":home.Home(screen, 0, "null", gameState), "menu":menu.Menu(screen, 0, {"eye_btn":eye_btn, "start_btn":start_btn, "end_btn":end_btn}, gameState,)}

play = True
while(play):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
        # if(event.type == pygame.KEYDOWN):
        #     event.unicode
        #This runs whatever room I'm in.
        states[gameState.getCurrentState()].run()
    

    pygame.display.flip()
    clock.tick(60)