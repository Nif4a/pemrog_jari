# GAME "jari jawa"
# rules :
# terdapat 2 player
# permainan dilakukan bergilir saling berganti-ganti antara player_1 dan player_2
# masing-masing player memiliki 2 tangan dengan jumlah jari masing-masing tangan lengkapnya 5(kiri) + 5(kanan) = 10
# 
# beberapa aturan : 
# game dimulai, masing-masing player memiliki 1 jari kiri dan 1 jari kanan. giliran pertama ditentukan dengan random
# player yang mendapat giliran menambahkan jumlah jari salah satu tanganya kepada player lawannya sebanyak jumlah jari pada tangan yang ia pakai untuk menambahkan
# player tidak boleh memilih tangannya yang jumlah jarinya sedang 0
# player tidak boleh menambahkan pada tangan lawan yang jumlah jarinya sedang 0
# contoh misal A = [3,2] dan B = [1,3], player lalu memilih tangannya yang R (2) untuk dijumlahkan pada tangan lawan L (3), maka setelah dilakukan penambahan giliran berganti pada player lawan dan kondisi tangan sekarang A = [3,2] dan B = [3,3]
# ketika jumlah jari pada salah satu tangan adalah 5, maka secara otomatis jumlah jari pada tangan tsb akan menjadi 0
# ketika jumlah jari pada salah satu tangan adalah >5 misal x, maka secara otomoatis jumlah jari pada tangan tsb akan menjadi x-5
# ketika salah satu tangan berjari 0 dan tangan yang lain berjumlah jari genap maka bisa melakukan "pecah" yakni yang awalnya [2,0] --> [1,1] atau [0,4] --> [2,2] dan pecah hanya bisa dilakukan saat mendapat giliran (memakai giliran) 
# permainan berakhir ketika salah satu pemain kedua tangannya jumlah jarinya 0, maka pemain yg jumlah jarinya 0 tsb yg memenangkan game ini

from modul_jari import *
import random
import pygame

pygame.init()
pygame.mixer.init()

# declare warna
putih = (255, 255, 255)
hitam = (0, 0, 0)
birumuda = (100,149,237)
abu = (120,120,120)

# font
custom_font = pygame.font.Font('font/pixely[1].ttf', 24)
font_jawa = pygame.font.Font('font/kemasyuran_jawa.ttf', 24)

# upload gambar
jari_kiri = [pygame.image.load('gambar/0_kiri.png'),pygame.image.load('gambar/1_kiri.png'),pygame.image.load('gambar/2_kiri.png'),pygame.image.load('gambar/3_kiri.png'),pygame.image.load('gambar/4_kiri.png')]
jari_kanan = [pygame.image.load('gambar/0_kanan.png'),pygame.image.load('gambar/1_kanan.png'),pygame.image.load('gambar/2_kanan.png'),pygame.image.load('gambar/3_kanan.png'),pygame.image.load('gambar/4_kanan.png')]
bandung = pygame.image.load('gambar/bandung.png')
bg = pygame.image.load('gambar/bg.png')

# tampilan screen menu
panjang_layar, lebar_layar = 800, 450
layar = pygame.display.set_mode((panjang_layar, lebar_layar))
pygame.display.set_caption("Jari Jawa menu")

# tampilan screen main
panjang_layar, lebar_layar = 800, 450
layar = pygame.display.set_mode((panjang_layar, lebar_layar))
pygame.display.set_caption("Jari Jawa v1")

# audio 
pygame.mixer.music.load('audio/bgm.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()

# inisiasi nilai jari awal masing-masing player adalah 1
player_1 = (1,1)
player_2 = (1,1)
gilir = random.randint(1,2)
isJalan = True
while isJalan:
    
    isRun = True
    while isRun:
        
        layar.blit(pygame.transform.scale(bg,(800,450)), (0,0))
        layar.blit(Transform(bandung),(0,50))
        layar.blit(Transform(flipimg(bandung)),(600,50))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                isRun = False
        
        # interface player
        giliran2(gilir,layar,font_jawa)
        status2(player_1,player_2,layar,jari_kiri,jari_kanan)
        
        pygame.display.flip()
        pygame.display.update()
        
        # proses game
        
        if gilir == 1:
            nilai = inputan(player_1,player_2)
            player_1,player_2 = masukan0(nilai,player_1,player_2)
            gilir = 2
            
        elif gilir == 2:
            nilai = inputan(player_2,player_1)
            player_2,player_1 = masukan0(nilai,player_2,player_1)
            gilir = 1    
        
        else:
            print("ga mungkin else ga sih")
        
        # cek kemenangan
        if cek0(player_1):
            win1(player_1,player_2)
            isRun = False
        if cek0(player_2):
            win2(player_1,player_2)
            isRun = False
        
        pygame.display.flip()
        pygame.display.update()
    
pygame.quit()