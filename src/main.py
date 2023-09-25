import pygame
import sys
from config import *

# Inicializar todos los modulos
pygame.init()

# Duración de cada iteración
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Tamaño de pantalla (superficie)
screen = pygame.display.set_mode(size_screen)
# Nombre del juego
pygame.display.set_caption("Primer Jueguito")
# Cambiar color
screen.fill(CUSTOM)

# Variable de control
is_running = True

# Crear objeto rectangulo
rect_1 = pygame.Rect(0, 0, 200, 100)

while is_running:
    clock.tick(FPS)
    # Detectar los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
         
    # pygame.draw.rect(donde?, color?, rect, borde?)
    pygame.draw.rect(screen, RED, rect_1)
         
         
    # Actualizar los elementos, puede ser flip o --> update()
    pygame.display.flip()
            
pygame.quit()
sys.exit()
            