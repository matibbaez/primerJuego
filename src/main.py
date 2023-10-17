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

draw = pygame.draw

# Direcciones
# ---> Up right
UR = 9
# ---> Down Right
DR = 3
# ---> Down Left
DL = 1
# ---> Up Left
UL = 7

# Creo el rectangulo
block = pygame.Rect(300, 500, 100, 50)
block_color = RED
block_dir = UR

radio = 50
alto = 100
ancho = 200

# Variable de control
is_running = True

while is_running:
    clock.tick(FPS)
    # ---> Detectar los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
         
    # ---> Actualizar los elementos
    
    # Cuando choco con el lateral derecho
    if block.right == width:
        if block_dir == DR:
            block_dir = DL
        elif block_dir == UR:
            block_dir = UL
    # Cuando choco con el lateral izquierdo
    elif block.left <= 0:
        if block_dir == DL:
            block_dir = DR
        elif block_dir == UL:
            block_dir = UR
    # Cuando choco con la parte inferior
    elif block.bottom >= height:
        if block_dir == DR:
            block_dir = UR
        elif block_dir == DL:
            block_dir = UL
    # Cuando choco con la parte superior
    elif block.top <= 0:
        if block_dir == UR:
            block_dir = DR
        elif block_dir == UL:
            block_dir = DL
    
    # Movimiento del bloque de acuerdo a su direccion
    if block_dir == DR:
        block.top += SPEED
        block.left += SPEED
    elif block_dir == DL:
        block.left -= SPEED
        block.top += SPEED
    elif block_dir == UL:
        block.left -= SPEED
        block.top -= SPEED
    elif block_dir == UR:
        block.left += SPEED
        block.top -= SPEED
    
    # ---> Dibujar pantalla
    screen.fill(BLACK)
    draw.rect(screen, block_color, block)
    
    # ---> Actualizar pantalla, puede ser flip o update()
    pygame.display.flip()
            
pygame.quit()
sys.exit()
            