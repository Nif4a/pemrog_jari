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

# tampilan screen menu
panjang_layar, lebar_layar = 800, 450
layar = pygame.display.set_mode((panjang_layar, lebar_layar))
pygame.display.set_caption("Jari Jawa")

# audio 
pygame.mixer.music.load('audio/bgm.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()

# game variabel
isMenu = False
isJalan = True
main = False
diff = "menu"

# game loop
while isJalan:
    
    layar.fill(abu)
    
    # cek main menu
    if main:
        isRun = True
        gilir = random.randint(1,2)
        player_1 = (1,1); player_2 = (1,1)
        varMasukan = (False,False,False)  #(kanan,kiri,pecah)
        varTujuan = (False,False)
        
        while isRun:
            layar.blit(pygame.transform.scale(bg,(800,450)), (0,0))
            layar.blit(Transform(bandung),(0,50))
            layar.blit(Transform(flipimg(bandung)),(600,50))
            
            if diff == "player":
                keys = pygame.key.get_pressed()
                giliran_2(gilir,layar,font_jawa)    
                status_2(player_1,player_2,layar,jari_kiri,jari_kanan)
                
                pygame.display.update()
                
                
                # proses game
                if gilir == 1:
                    if cekVarMasukan(varMasukan):
                        # mekanisme tujuan
                        temp = tujuan_2(player_2,custom_font,putih,layar,keys)
                        varTujuan = temp[0]
                        valid2 = temp[1]
                        if valid2:
                            nilai = (konversiMasukan(varMasukan),konversiTujuan(varTujuan))
                            player_1,player_2 = masukan0(nilai,player_1,player_2)
                            varMasukan,varTujuan = reset()
                            gilir = 2
                        else:
                            varTujuan = (False,False)
                    else:
                        # mekanisme masukan
                        temp = inputan_2(player_1,custom_font,putih,layar,keys)
                        varMasukan = temp[0]
                        valid = temp[1]
                        if valid:
                            if varMasukan == (False,False,True):
                                nilai = ("P","B")
                                player_1,player_2 = masukan0(nilai,player_1,player_2)
                                varMasukan,varTujuan = reset()
                                gilir = 2
                        else:
                            varMasukan = (False,False,False)                 
                elif gilir == 2:
                    if cekVarMasukan(varMasukan):
                        # mekanisme tujuan
                        temp = tujuan_2(player_1,custom_font,putih,layar,keys)
                        varTujuan = temp[0]
                        valid2 = temp[1]
                        if valid2:
                            nilai = (konversiMasukan(varMasukan),konversiTujuan(varTujuan))
                            player_2,player_1 = masukan0(nilai,player_2,player_1)
                            varMasukan,varTujuan = reset()
                            gilir = 1
                        else:
                            varTujuan = (False,False)
                    else:
                        # mekanisme masukan
                        temp = inputan_2(player_2,custom_font,putih,layar,keys)
                        varMasukan = temp[0]
                        valid = temp[1]
                        if valid:
                            if varMasukan == (False,False,True):
                                nilai = ("P","B")
                                player_2,player_1 = masukan0(nilai,player_2,player_1)
                                varMasukan,varTujuan = reset()
                                gilir = 1
                        else:
                            varMasukan = (False,False,False)  
                else:
                    print("ga mungkin else ga sih")
                
                # cek kemenangan
                if cek0(player_1):
                    win1_2(player_1,player_2,custom_font,putih,layar)
                    isRun = False
                if cek0(player_2):
                    win2_2(player_1,player_2,custom_font,putih,layar)
                    isRun = False          
                if keys[pygame.K_ESCAPE]:
                    isRun = False
                               
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isRun = False
                    isJalan = False
            
    else:
        # check masuk menu / tidak
        if isMenu == True:
            layar.blit(scaling(Transform2(tombol2[0]),2), (300,50))
            layar.blit(scaling(Transform2(tombol2[1]),2), (50,250))
            layar.blit(scaling(Transform2(tombol2[2]),2), (300,250))
            layar.blit(scaling(Transform2(tombol2[3]),2), (550,250))
            drawTeks("Tekan esc untuk keluar permainan",custom_font,putih,130,400,layar)
            if keys[pygame.K_p]:
                isMenu = False
                diff = "player"; main = True
            if keys[pygame.K_1]:
                isMenu = False
                diff = "easy"; main = False
            if keys[pygame.K_2]:
                isMenu = False
                diff = "medium"; main = False
            if keys[pygame.K_3]:
                isMenu = False
                diff = "hard"; main = False
            if keys[pygame.K_ESCAPE]:
                isJalan = False
            
        else:
            drawTeks("TEKAN SPASI UNTUK MELANJUTKAN", custom_font, putih, 130, 185, layar)

    # pengatur event
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            isMenu = True
        if event.type == pygame.QUIT:
            isJalan = False
    
    pygame.display.update()
    
pygame.quit()