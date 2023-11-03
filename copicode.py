import pygame
pygame.init()

screen = pygame.display.set_mode((1280,720))

screen.fill("green")

red = 240; green = 120; blue = 50
screen.fill((red,green,blue))

screen.get_width(); screen.get_height()

bg = pygame.image.load('bg.jpg')
screen.blit(bg, (0,0))

class kotak(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self):
        object.__init__(self)
        self.image = screen(60,40)
        self.rect = bg(10,10,40,20)

