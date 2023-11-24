import pygame
pygame.init()

# declare warna
putih = (255, 255, 255)
hitam = (0, 0, 0)
birumuda = (100,149,237)

# font
custom_font = pygame.font.Font('font/pixely[1].ttf', 24)
contoh = "contoh1"

# tampilan screen
panjang_layar, lebar_layar = 800, 450
layar = pygame.display.set_mode((panjang_layar, lebar_layar))
pygame.display.set_caption("Jari Jawa v1")

# loop game
isRun = True
while isRun:

    layar.fill(birumuda)

    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False  
    
    # update screen tiap event
    pygame.display.update()

pygame.quit()