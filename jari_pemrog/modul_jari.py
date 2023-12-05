import pygame
putih = (255, 255, 255)
hitam = (0, 0, 0)
birumuda = (100,149,237)
abu = (120,120,120)

# bagian pygame
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


# fungsi cek kemenangan
def cek0(player):
    x,y = player
    if x == 0 and y == 0:
        return True
    else:
        return False 
    
# fungsi cek apakah jari sudah 5
def cek5(player):
    x,y = player
    if x == 5:
        x = 0
    if y == 5:
        y = 0
    return x,y

# fungsi cek apakah jari lebih dari 5
def lebih5(player):
    x,y = player
    if x > 5:
        x = x-5
    if y > 5:
        y = y-5
    return x,y  

# cek pecah
def cekpecah(player):
    x,y = player
    if x == 0 and y%2 == 0:
        return True
    elif x%2 == 0 and y == 0:
        return True
    else:
        if x == 0 or y == 0:
            print("jari sekarang berjumlah ganjil")
        else: 
            print("jari salah satu tangan tidak 0")
        return False

# cek pecah2
def cekpecah2(player):
    x,y = player
    if (x == 2 and y == 0) or (x == 0 and y ==2):
        return True
    else:
        return False

# fungsi untuk yang pecah 2
def pecah2(player):
    x,y = player
    if (x == 2 and y == 0) or (x == 0 and y ==2):
        x,y = 1,1
    return x,y

# fungsi untuk yang pecah 4
def pecah4(player):
    x,y = player
    if (x == 4 and y == 0) or (x == 0 and y == 4):
        x,y = 2,2
    return x,y

# procedure cetak jari player
def status(player1,player2):
    a,b = player1; c,d = player2
    print(f"""--------
 [{a} {b}]
 [{c} {d}]
--------""") 

def status2(player1,player2,layar,jkir,jkan):
    a,b = player1; c,d = player2
    layar.blit(Transform(rotate(jkir[c])),(200,0))
    layar.blit(Transform(rotate(jkan[d])),(400,0))
    layar.blit(Transform(jkan[a]),(200,250))
    layar.blit(Transform(jkan[b]),(400,250))
    
# cek giliran 
def giliran(angka):
    if angka == 1:
        print("\n## giliran player 1 ##")
    if angka == 2:
        print("\n## giliran player 2 ##")

def giliran2(angka,layar,font):
    teks = font.render("giliran player "+str(angka), True, hitam)
    layar.blit(teks, (10,10))
    
    
# masukan dari lain
def masukan0(nilai,playermain,playerlawan):
    x,y = nilai
    a,b = playermain
    c,d = playerlawan
    if x == "P":
        if cekpecah2(playermain):
            a,b = pecah2(playermain)
        else:
            a,b = pecah4(playermain)
    else:
        c,d = masukan(playermain,playerlawan,x,y)
    
    return ((a,b),(c,d))

# cek sisa jari masukan
def sisa(player,jari):
    x,y = player
    if jari == "R" and y == 0:
        print("jari yang anda pilih bernilai 0")
        return True
    elif jari == "L" and x == 0:
        print("jari yang anda pilih bernilai 0")
        return True
    else:
        return False

def cektujuan(player,nilai):
    x,y = player
    if nilai == "R" and y == 0:
        print("nilai jari yang anda tuju 0")
        return True
    elif nilai == "L" and x == 0:
        print("nilai jari yang anda tuju 0")
        return True
    else:
        return False        
    
# masukan player
def masukan(playermain,playerlawan,masukan,tujuan):
    a,b = playermain; c,d = playerlawan
    if masukan == "R" and tujuan == "R":
        d += b
    elif masukan == "R" and tujuan == "L":
        c += b
    elif masukan == "L" and tujuan == "R":
        d += a
    elif masukan == "L" and tujuan == "L":
        c += a
    else:
        c,d = c,d
    
    # di cek nilai hasilnya
    c,d = cek5((c,d))
    c,d = lebih5((c,d))
    
    return (c,d)

# proses input
def inputan(player,player2):
    cek = False
    while cek == False:
        jariinput = input('pilih jari "R/L" atau pecah "P": ')
        cek2 = sisa(player,jariinput)
        if (jariinput == "R" or jariinput == "L") and cek2 == False:            
            cek3 = True
            while cek3:
                jarioutput = input('pilih jari lawan "R/L": ')
                cek3 = cektujuan(player2,jarioutput)
                if jarioutput != "R":
                    if jarioutput != "L":
                        print("Anda mungkin typo, silahkan coba lagi")
                        cek3 = True
                cek = True
            return (jariinput,jarioutput)
        elif jariinput == "P":
            cek = cekpecah(player)
        elif cek2 == False:
            print("Anda mungkin typo, silahkan coba lagi")
    return ("P","P")

def inputan2(player,player2,kiri,kanan):
    cek = False
    while cek == False:
        jariinput = input('pilih jari "R/L" atau pecah "P": ')
        cek2 = sisa(player,jariinput)
        if (jariinput == "R" or jariinput == "L") and cek2 == False:            
            cek3 = True
            while cek3:
                jarioutput = input('pilih jari lawan "R/L": ')
                cek3 = cektujuan(player2,jarioutput)
                cek = True
            return (jariinput,jarioutput)
        elif jariinput == "P":
            cek = cekpecah(player)
        elif cek2 == False:
            print("Anda mungkin typo, silahkan coba lagi")
    return ("P","P")

def win1(p1,p2):
    print("\n\n## ## ## ## ##")
    status(p1,p2)
    print("selamat player 1 memenangkan game")   

def win2(p1,p2):
    print("\n\n## ## ## ## ##")
    status(p1,p2)
    print("selamat player 2 memenangkan game")