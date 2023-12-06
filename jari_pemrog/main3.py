import pygame
pygame.init()

# declare warna
putih = (255, 255, 255)
hitam = (0, 0, 0)
birumuda = (100,149,237)
abu = (120,120,120)


# tampilan screen menu
panjang_screen, lebar_screen = 800, 450
screen = pygame.display.set_mode((panjang_screen, lebar_screen))
pygame.display.set_caption("Jari Jawa")

# font
pixel1 = pygame.font.Font('font/pixely[1].ttf', 24)
pixel2 = pygame.font.Font('font/pixely[1].ttf', 60)
font_jawa1 = pygame.font.Font('font/kemasyuran_jawa.ttf', 24)
font_jawa2 = pygame.font.Font('font/kemasyuran_jawa.ttf', 40)

def drawTeks(teks, font, warna, x, y):
    img = font.render(teks, True, warna)
    screen.blit(img, (x,y))

# game variabel
isJalan = True
isMenu = False


# game loop
while isJalan:
    
    screen.fill(birumuda)
    
    drawTeks("TEKAN SPASI UNTUK MELANJUTKAN", pixel2, putih, 130, 185)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_SPACE:
                print("PAUSE")
        if event.type == pygame.QUIT:
            isJalan = False

    pygame.display.update()

pygame.quit()