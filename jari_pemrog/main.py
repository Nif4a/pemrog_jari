import pygame
from modul_jari import *
pygame.init()

# declare warna
putih = (255, 255, 255)
hitam = (0, 0, 0)
birumuda = (100,149,237)

# font
custom_font = pygame.font.Font('font/pixely[1].ttf', 24)
contoh = "contoh1"

# upload gambar
jari_kiri = [pygame.image.load('gambar/1_kiri.png'),pygame.image.load('gambar/2_kiri.png'),pygame.image.load('gambar/3_kiri.png'),pygame.image.load('gambar/4_kiri.png')]
jari_kanan = [pygame.image.load('gambar/1_kanan.png'),pygame.image.load('gambar/2_kanan.png'),pygame.image.load('gambar/3_kanan.png'),pygame.image.load('gambar/4_kanan.png')]
bandung = pygame.image.load('gambar/bandung.png')

# tampilan screen
panjang_layar, lebar_layar = 800, 450
layar = pygame.display.set_mode((panjang_layar, lebar_layar))
pygame.display.set_caption("Jari Jawa v1")

# init var
tertekan = False
player1 = (1,1)
kiri = False
kanan = True

def bacaJari(player):
    x,y = player
    return x-1,y-1
    
def Transform(gambar):
    ukuran = (200,200)
    gambar = pygame.transform.scale(gambar, ukuran)
    return gambar

def Tertekan(gambar,posisi):
    global tertekan
    aksi = False
    
    rect = gambar.get_rect()
    if rect.collidepoint(posisi):
        if pygame.mouse.get_pressed()[0] == 1 and tertekan == False:
            tertekan = True; aksi = True
    if pygame.mouse.get_pressed()[0] == 0:
        tertekan = False
    return aksi

# loop game
isRun = True
while isRun:

    # init layar
    layar.fill(birumuda)
    posisi = pygame.mouse.get_pos()
    a,b = bacaJari(player1)
    
    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
        
           
    # program main
    
    # define draw
    
      
    
    # draw
    
    teks = custom_font.render(str(posisi), True, hitam)
    layar.blit(teks,(10,10))
    
    # draw
    x,y = posisi
    if Tertekan(Transform(jari_kiri[a]),(x-200,y-250)):
        layar.blit(Transform(jari_kiri[a]), (200,240))
    else:
        layar.blit(Transform(jari_kiri[a]), (200,250))
    
    if Tertekan(Transform(jari_kanan[b]),(x-400,y-250)):
        layar.blit(Transform(jari_kanan[b]), (400,240))
    else:
        layar.blit(Transform(jari_kanan[b]), (400,250))
        
     
    
    
    
    pygame.display.flip()   
    
    # update screen tiap event
    pygame.display.update()

pygame.quit()