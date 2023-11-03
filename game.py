import pygame

pygame.init()
x=1280
y=720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("warna bergerak")

dx = 20
dy = 20
width = 50
height = 50
move = 6

isRun = True
while isRun:
    pygame.time.delay(20)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    screen.fill("black")
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        dy -= move
    if keys[pygame.K_DOWN]:
        dy += move
    if keys[pygame.K_LEFT]:
        dx -= move
    if keys[pygame.K_RIGHT]:
        dx += move
    
    
    pygame.draw.rect(screen, (255, 0, 0), (dx, dy, width, height))
    pygame.display.update()


pygame.quit()