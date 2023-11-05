import pygame
pygame.init()

layar = pygame.display.set_mode((800,480))
pygame.display.set_caption("pingpong")

isRun = True
while isRun:
    pygame.time.delay(20)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    
    keys = pygame.key.get_pressed()
    
pygame.quit()
    
