import pygame
pygame.init()

class JariJawa:
    def __init__(self):
        pygame.init()
        
        # tampilan screen
        self.panjang_layar, self.lebar_layar = 800, 450
        self.layar = pygame.display.set_mode((self.panjang_layar, self.lebar_layar))
        pygame.display.set_caption("jari jawa v1")
        self.putih = (255, 255, 255)
        self.hitam = (0, 0, 0)
        
        # font
        self.custom_font = pygame.font.Font('font/pixely[1].ttf', 32)
        self.contoh = "Agus231#"
        
        # insialisasi run
        
    
    def draw_objek(self):
        
        # draw gambar
        self.jari1 = pygame.image.load('gambar/Jari1Kiri.png')
        
        
        # draw teks ke layar
        teks = self.custom_font.render(self.contoh, True, self.putih)
        self.layar.fill(self.hitam)
        self.layar.blit(teks, (self.panjang_layar//2,30))
        
        # draw teks posisi
        teks2 = self.custom_font.render(str(self.posisi), True, self.putih)
        self.layar.blit(teks2, (10,10))
        pygame.display.flip()
        
    
        
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