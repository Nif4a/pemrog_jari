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

from jari import *
import random

# inisiasi nilai jari awal masing-masing player adalah 1
player_1 = (1,1)
player_2 = (1,1)
gilir = random.randint(1,2)
print(f"player {gilir} dapat memulai game terlebih dahulu")    

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
        print("ga mungkin else ga sih")
    
    # cek kemenangan
    if cek0(player_1):
        win1(player_1,player_2)
        isRun = False
    if cek0(player_2):
        win2(player_1,player_2)
        isRun = False