import PIL
import pygame

pygame.init()
clock = pygame.time.Clock()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

base_font = pygame.font.Font(None, 32)
starter_text = "Empty Eyes Can Still Dream"


run = True
menu = True
play = True

# while(run):
#     while(menu):
#         ans = input()
#         if(ans == "1"):
#             play = True
#             menu = False
#         if(ans == "2"):
#             menu = False
#             run = False
while(play):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
    screen.fill((23,34,78))
    text_surface = base_font.render(starter_text, True, (255,255,255))
    screen.blit(text_surface,(150,275))

    #Have the eye image here


    #Then have the player click the start button to get into the first room and the actual story.


    pygame.display.flip()
    clock.tick(60)