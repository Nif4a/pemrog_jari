from modul_jari import *
import random
import pygame
import time

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
                ai_level = "player"; main = True
            if keys[pygame.K_1]:
                isMenu = False
                ai_level = "easy"; main = True
            if keys[pygame.K_2]:
                isMenu = False
                ai_level = "medium"; main = True
            if keys[pygame.K_3]:
                isMenu = False
                ai_level = "hard"; main = True
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