import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario Bros")

# Cargar imágenes y sonidos
# Por ejemplo, cargar imágenes de Mario
try:
    mario_image = pygame.image.load("mario_bro.png").convert_alpha()
except pygame.error:
    print("Error: 'mario.png' not found. Please make sure the image is in the same directory.")
    sys.exit()

# Cargar sonido de salto
try:
    jump_sound = pygame.mixer.Sound("ringtones-super-mario-bros.mp3")
except pygame.error:
    print("Error: 'jump.wav' not found. Please make sure the sound file is in the same directory.")
    sys.exit()


class Mario:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = mario_image
        self.speed = 5
        self.is_jumping = False
        self.jump_height = 20
        self.gravity = 1
        self.y_vel = 0
        self.rect = self.image.get_rect()

    def move(self, direction):
        # Actualizar posición de Mario según la dirección
        if direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed

        # Mantener a Mario dentro de los límites de la pantalla
        if self.x < 0:
            self.x = 0
        elif self.x + self.image.get_width() > screen_width:
            self.x = screen_width - self.image.get_width()

    def jump(self):
        # Realizar el salto de Mario
        if not self.is_jumping:
            self.is_jumping = True
            self.y_vel = -self.jump_height
            jump_sound.play()  # Reproducir sonido de salto

    def update_gravity(self):
        # Aplicar gravedad
        self.y_vel += self.gravity
        self.y += self.y_vel

        # Si Mario toca el suelo, reiniciar el salto
        if self.y + self.image.get_height() >= screen_height:
            self.y = screen_height - self.image.get_height()
            self.y_vel = 0
            self.is_jumping = False

    def draw(self, screen):
        # Dibujar Mario en la pantalla
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.image, self.rect)

# Inicializar objetos
# Ensure mario_image is loaded before trying to access its height
if 'mario_image' in locals():
    mario = Mario(100, screen_height - mario_image.get_height())
else:
    print("Mario image not loaded, cannot initialize Mario object.")
    sys.exit()

# Bucle principal del juego
running = True
while running:
    # Manejar eventos del usuario
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mario.move("left")
            if event.key == pygame.K_RIGHT:
                mario.move("right")
            if event.key == pygame.K_SPACE:
                mario.jump()

    # Actualizar juego
    mario.update_gravity()

    # Dibujar juego
    screen.fill((0, 0, 0))  # Limpiar la pantalla
    mario.draw(screen)
    pygame.display.flip()  # Actualizar la pantalla

# Salir de Pygame
pygame.quit()
sys.exit()