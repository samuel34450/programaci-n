rojo= (255,0 ,0 ,0)
black=(0,0,0)
import pygame
#importo librerias
import sys
import random
# Constantes
ANCHO = 1000#ancho
ALTO = 900

class Asteroide(pygame.sprite.Sprite):   
    def __init__ (self):
        self.x=random.randint(50, ANCHO -50)
        self.y=0
        self.velocidad=random.randint (2, 5)
        self.radio= 20
    def mover(self):
        self.y+=self.velocidad
    def dibujar(self,superficie):
        pygame.draw .circle(superficie, black ,(self.x, self.y),self.radio)

def main():
    pygame.init()#si no lo uso no funciona nada
    VENTANA = pygame.display.set_mode((ANCHO, ALTO))# creamos la ve
    pygame.display.set_caption("objeto cae")
    
    asteroide=Asteroide()  #definimos 
    
    # crear grupo de sprites
    asteroides = pygame.sprite.Group()
    
    for i in range(10):
        asteroide = Asteroide()
        asteroides.add(asteroide)
    
    while True:
        VENTANA.fill((rojo))
        
        asteroides.update()
        asteroides.draw(VENTANA)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        asteroide.dibujar(VENTANA) #dibujar el aseroide en la ventana
        pygame.display.flip()
        pygame.display.update()
        pygame.time.Clock(). tick(80)
                                                     
if __name__ == "__main__":#si no tengo errores se ejecuta main
    main()