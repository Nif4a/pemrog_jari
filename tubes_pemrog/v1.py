# GAME "jari jawa"
# rules :
# terdapat 2 player
# giliran saling berganti-ganti antara player_1 dan player_2
# masing-masing player memiliki 2 tangan berbentuk tuple integer (a.b)

from jari import *
import random

# inisiasi nilai jari awal masing-masing player adalah 1
player_1 = (1,1)
player_2 = (1,1)
gilir = random.randint(1,2)
print(f"player {gilir} bisa memulai permainan duluan")    

isRun = True
while isRun:
    
    # interface player
    giliran(gilir)
    status(player_1,player_2)
    
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
        print("ga mungkin else")
    
    # cek kemenangan
    if cek0(player_1):
        win1(player_1,player_2)
        isRun = False
    if cek0(player_2):
        win2(player_1,player_2)
        isRun = False
        