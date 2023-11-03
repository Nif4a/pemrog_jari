import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("nama game")

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

    if keys[pygame.K_UP] and dy > 5:
        dy -= move
    if keys[pygame.K_DOWN] and dy < (715 - height):
        dy += move
    if keys[pygame.K_LEFT] and dx > 5:
        dx -= move
    if keys[pygame.K_RIGHT] and dx < (1275 - width):
        dx += move
    if keys[pygame.K_SPACE]:
        isJump = True
    
    
    pygame.draw.rect(screen, (255, 0, 0), (dx, dy, width, height))
    pygame.display.update()


pygame.quit()