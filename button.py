import pygame

class Button():
    def __init__(self, x, y, image, size) -> None:
        self.__x = x
        self.__y = y
        self.image = image
        self.clicked = False
        if(size != 0):
            self.image = pygame.transform.scale(self.image, (size[0], size[1]))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.__x,self.__y)
            
        
    def draw(self, surface):
        action = False
        #Get moust position
        pos = pygame.mouse.get_pos()
        if(self.rect.collidepoint(pos)):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                action = True
                
            # if pygame.mouse.get_pressed()[0] and self.clicked == True:
            #     print("The Button Has Already Been Clicked")
            
            if pygame.mouse.get_pressed()[0] == False:
                self.clicked = False
        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action