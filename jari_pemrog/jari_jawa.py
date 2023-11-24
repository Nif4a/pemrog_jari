import pygame
pygame.init()

class Jari():
    def __init__(self, x, y, iMage):
        self.iMage = iMage
        self.rect = self.iMage.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    
    def draw_jari(self, screen):
        aksi = False
        
        # posisi mouse
        posisi = pygame.mouse.get_pos()
        if self.rect.collidepoint(posisi):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                aksi = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        # draw jari di screen
        screen.blit(self.iMage, (self.rect.x, self.rect.y))
        return aksi
    
class JariJawa():
    def __init__(self):
        pygame.init()
        
        # tampilan screen
        panjang_layar, lebar_layar = 800, 450
        self.layar = pygame.display.set_mode((panjang_layar, lebar_layar))
        pygame.display.set_caption("jari jawa v1")
        
        # declare warna
        self.putih = (255, 255, 255)
        self.hitam = (0, 0, 0)
        self.birumuda = (100,149,237)
        
        # font
        self.custom_font = pygame.font.Font('font\pixely[1].ttf', 20)
        self.contoh = "contohTeks0#"
                
    
    def draw_objek(self):
        
        # draw gambar
        jari1 = pygame.image.load('gambar/Jari1Kiri.jpg').convert()
        #self.layar.blit(jari1, (400,200))
                             
        # draw teks ke layar
        teks = self.custom_font.render(self.contoh, True, self.putih)
        self.layar.fill(self.birumuda)
        self.layar.blit(teks, (560,10))
        
        # draw jari
        tombol_jari1 = Jari(400, 200, jari1)
        if tombol_jari1.draw_jari(self.layar) == True:
            print("OK")
            
        #draw teks posisi
        teks2 = self.custom_font.render(str(self.posisi), True, self.hitam)
        self.layar.blit(teks2, (10,10))
        pygame.display.flip() 
        pygame.display.update()

          
        
    def isi_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRun = False      
        
        self.klik_kiri = pygame.mouse.get_pressed()[0]
        self.klik_kanan = pygame.mouse.get_pressed()[2]
        self.posisi = pygame.mouse.get_pos()        
    
    
    def run(self):
        self.isRun = True
        while self.isRun:
            self.isi_event()
            self.draw_objek()
        pygame.quit()

if __name__ == "__main__":
    game = JariJawa()
    game.run()