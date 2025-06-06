import pygame
from pygame.locals import *
import sys
import random

verde = (0, 255, 0)
negro = (0, 0, 0)

SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680

class Enemigo1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ene1 = pygame.image.load('enemy.png')
        self.ene1 = pygame.transform.scale(self.ene1, (50, 50))
        self.ene1 = pygame.transform.flip(self.ene1, True, False)
        self.pose = self.ene1.get_rect()
        x_rand = random.randint(0, SCREEN_WIDTH - 50)
        y_rand = random.randint(300, 440)
        self.pose.topleft = (x_rand, y_rand)

    def dibujar(self, screen):
        screen.blit(self.ene1, self.pose)



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("tutorial de pygame de crear ventana")
    screen.fill(verde)
    
    mi_imagen_actual = pygame.image.load('mario_bro.png')
    mi_imagen_corrinedo = pygame.image.load("mario_bro2.png")
    mi_imagen_actual = pygame.transform.scale(mi_imagen_actual,(50, 50))
    mi_imagen_corrinedo = pygame.transform.scale(mi_imagen_corrinedo,(50, 50))
    mi_imagen_actual2 = pygame.transform.flip(mi_imagen_actual, True, False)
    mi_imagen_corrinedo2 = pygame.transform.flip(mi_imagen_corrinedo, True, False)
    
    grupoE = pygame.sprite.Group()
    enemigo = Enemigo1()
    grupoE.add(enemigo)
    
    ima_rect = mi_imagen_actual.get_rect()
    ima_rect.center = (SCREEN_WIDTH // 2, 460)

    correr = [mi_imagen_corrinedo, mi_imagen_actual]
    correr2 = [mi_imagen_corrinedo2, mi_imagen_actual2]

    fondo = pygame.image.load('1fondo.jpg')
    fondo = pygame.transform.scale(fondo, (SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.mixer.music.load('ringtones-super-mario-bros.mp3')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1, 0.0)
    
    inter = 0

    is_jumping = False
    jump_speed = -15
    vertical_velocity = 0
    ground_level = 440
    
    caca = pygame.Rect(1070, 440, 50, 50)
    
    reloj = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping:
                    is_jumping = True
                    vertical_velocity = jump_speed

        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_d]:
            mi_imagen_actual = correr[inter % 2]
            ima_rect.x += 5
        elif tecla[pygame.K_a]:
            mi_imagen_actual = correr2[inter % 2]
            ima_rect.x -= 5

        if is_jumping:
            ima_rect.y += vertical_velocity
            vertical_velocity += 1
            if ima_rect.y >= ground_level:
                ima_rect.y = ground_level
                is_jumping = False
                vertical_velocity = 0

        screen.blit(fondo, (0, 0))
        screen.blit(mi_imagen_actual, ima_rect)

        for ene in grupoE:
            ene.dibujar(screen)

        pygame.draw.rect(screen, verde, caca, 2)

        reloj.tick(40)
        pygame.display.update()
        inter += 1

if __name__ == "__main__":
    main()
