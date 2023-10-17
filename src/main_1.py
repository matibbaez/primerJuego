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

radio = 50
alto = 100
ancho = 200

pos_y = height // 2 - alto / 2
pos_x = 0

bajando = True
izquierda = True

# Variable de control
is_running = True

while is_running:
    clock.tick(FPS)
    # ---> Detectar los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
         
    # ---> Actualizar los elementos
    
    # ---> Bajando
    if bajando:
        if pos_y < height - alto:
            pos_y += SPEED
        else:
            bajando = False
    # ---> Subiendo
    else:
        if pos_y > 0:
            pos_y -= SPEED
        else: 
            bajando = True
    
    
    if izquierda:
        if pos_x < width - ancho:
            pos_x += SPEED
        else:
            izquierda = False
    else:
        if pos_x > 0:
            pos_x -= SPEED
        else:
            izquierda = True
    
    # ---> Dibujar pantalla
    screen.fill(BLACK)
    
    r = draw.rect(screen, RED, (300, pos_y, ancho, alto), 5)
    
    r_2 = draw.rect(screen, RED, (pos_x, 250, ancho, alto), 5)
            
    
    # r = draw.circle(screen, RED, (width // 2, pos_y), 50, 5)
    # draw.line(screen, RED, (0, 0), (r.center), 5)

    # draw.circle(screen, GREEN, (width - radio, radio), radio, 5)
    
    # draw.line(screen, RED, (0, 0), (width, height), 5)
    
    # r_elipse = draw.ellipse(screen, BLUE, (200, 300, 50, 100), 5)
    
    # r_poligono = draw.polygon(screen, BLUE, [(500, 150), (700, 50), (750, 350)], 7)
    
    # draw.rect(screen, ORANGE, r_poligono, 4)  
      
    # draw.rect(screen, ORANGE, r_elipse, 4)    
    
    # ---> Actualizar pantalla, puede ser flip o update()
    pygame.display.flip()
            
pygame.quit()
sys.exit()
            