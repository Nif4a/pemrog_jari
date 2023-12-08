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
import time 

pygame.init()
pygame.mixer.init()

# tampilan screen main
panjang_layar, lebar_layar = 800, 450
layar = pygame.display.set_mode((panjang_layar, lebar_layar))
pygame.display.set_caption("Jari Jawa v1")

# audio 
pygame.mixer.music.load('audio/bgm.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()

# inisiasi nilai jari awal masing-masing player adalah 1
player_1 = (1,1); player_2 = (1,1)
gilir = random.randint(1,2)
isJalan = True
ai_level = "medium"

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
    giliran_2(gilir,layar,font_jawa)
    status_2(player_1,player_2,layar,jari_kiri,jari_kanan)
    
    pygame.display.flip()
    pygame.display.update()
    
    # proses game
    
    if gilir == 1:  # Giliran AI
        if ai_level == "easy":
            ai_input = random.choice(["R", "L"])
            ai_output = random.choice(["R", "L"])
        elif ai_level == "medium":
            ai_input, ai_output = bestMove(player_1, player_2)
        elif ai_level == "hard":
            # Implementasi Minimax dengan depth yang lebih dalam
            ai_input, ai_output = bestMove(player_1, player_2)

        print(f"AI sedang memikirkan langkahnya...")
        time.sleep(2)  # Tambahkan delay 2 detik
        print(f"AI memilih jari {ai_input} untuk dimasukkan pada tangan lawan dengan jari {ai_output}")
        player_1, player_2 = masukan0((ai_input, ai_output), player_1, player_2)
        gilir = 2
        
    elif gilir == 2:  # Giliran manusia
        nilai = inputan(player_2, player_1)
        player_2, player_1 = masukan0(nilai, player_2, player_1)
        gilir = 1
    
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