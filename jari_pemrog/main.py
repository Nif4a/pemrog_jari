import pygame
from modul_jari import *
pygame.init()
pygame.mixer.init()

# declare warna
putih = (255, 255, 255)
hitam = (0, 0, 0)
birumuda = (100,149,237)
abu = (120,120,120)

# font
custom_font = pygame.font.Font('font/pixely[1].ttf', 24)

# upload gambar
jari_kiri = [pygame.image.load('gambar/0_kiri.png'),pygame.image.load('gambar/1_kiri.png'),pygame.image.load('gambar/2_kiri.png'),pygame.image.load('gambar/3_kiri.png'),pygame.image.load('gambar/4_kiri.png')]
jari_kanan = [pygame.image.load('gambar/0_kanan.png'),pygame.image.load('gambar/1_kanan.png'),pygame.image.load('gambar/2_kanan.png'),pygame.image.load('gambar/3_kanan.png'),pygame.image.load('gambar/4_kanan.png')]
bandung = pygame.image.load('gambar/bandung.png')
bg = pygame.image.load('gambar/bg.png')

# tampilan screen
panjang_layar, lebar_layar = 800, 450
layar = pygame.display.set_mode((panjang_layar, lebar_layar))
pygame.display.set_caption("Jari Jawa v1")

# audio 
pygame.mixer.music.load('audio/bgm.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()

# init variabel
tertekan = False
player1 = (1,1)
player2 = (1,1)
kiri = False
kanan = False
gilir = 1


def flipimg(gambar):
    gambar = pygame.transform.flip(gambar, True, False)
    return gambar
    
def bacaJari(player):
    x,y = player
    return x,y

def rotate(gambar):
    sudut = 180
    gambar = pygame.transform.rotate(gambar, sudut)
    return gambar
    
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

def TertekanLuar(gambar,posisi):
    global tertekan
    aksi = False
    
    rect = gambar.get_rect()
    if rect.collidepoint(posisi) == False:
        if pygame.mouse.get_pressed()[0] == 1 and tertekan == False:
            tertekan = True; aksi = True
    if pygame.mouse.get_pressed()[0] == 0:
        tertekan = False
    return aksi
        

# loop game
isRun = True
while isRun:

    # init layar
    layar.blit(pygame.transform.scale(bg,(800,450)), (0,0))
    posisi = pygame.mouse.get_pos()
    a,b = bacaJari(player1)
    c,d = bacaJari(player2)
    
    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            isRun = False
    
    layar.blit(Transform(bandung),(0,50))
    layar.blit(Transform(flipimg(bandung)),(600,50))
    
    # draw
    layar.blit(Transform(rotate(jari_kiri[a])),(200,0))
    layar.blit(Transform(rotate(jari_kanan[b])),(400,0))
        
    # draw
    #teks = custom_font.render(str(posisi), True, hitam)
    #layar.blit(teks,(10,10))
    teks = custom_font.render("JariJawa",True,putih)
    layar.blit(teks, (10,10))
    
    # draw
    # jari kiri
    x,y = posisi
    if Tertekan(Transform(jari_kiri[a]),(x-200,y-250)):
        layar.blit(Transform(jari_kiri[a]), (200,240))
        print("A")
        kiri = True
    elif Tertekan(Transform(jari_kanan[b]),(x-400,y-250)):
        layar.blit(Transform(jari_kanan[b]), (400,240))
        print("B")
        kanan = True
    else:
        pygame.time.delay(75)
        layar.blit(Transform(jari_kiri[a]), (200,250))
        layar.blit(Transform(jari_kanan[b]), (400,250))
        if Tertekan(Transform(rotate(jari_kiri[a])),(x-200,y)):
            c = c+a
        if Tertekan(Transform(rotate(jari_kanan[b])),(x-400,y)):
            d = d+a           
        # jari kiri dan kanan false
        if TertekanLuar(Transform(jari_kiri[a]),(x-200,y-250)) or TertekanLuar(Transform(jari_kanan[b]),(x-400,y-250)):
            print("AB")
            kiri = False
            kanan = False
    
    print(kiri,kanan)
    
    # giliran
    #if gilir == 1:
    #   nilai = inputan2(player1,player2,kiri,kanan)
    #    player_1,player_2 = masukan0(nilai,player_1,player_2)
    #    gilir = 2
    #elif gilir == 2:
    #    nilai = inputan2(player_2,player_1,kiri,kanan)
    #    player_2,player_1 = masukan0(nilai,player_2,player_1)
    #    gilir = 1
    
    # cek kemenangan
    if cek0(player1):
        win1 = custom_font.render("selamat player 1 memenangkan permainan",True,putih)
        layar.blit(win1,(20,20))
        isRun = False
    if cek0(player2):
        win2 = custom_font.render("selamat player 2 memenangkan permainan",True,putih)
        layar.blit(win2,(20,20))
        isRun = False
        
    # update
    pygame.display.flip()   
    pygame.display.update()

pygame.quit()