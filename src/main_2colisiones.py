import sys
import pygame
from config import *
from aleatorias import *
from random import randint, randrange
from pygame import display, time, draw, event
 
def detectar_colision(rec_1, rec_2):
    colision = False
    if (
        punto_en_rectangulo(rec_1.topleft, rec_2) or
        punto_en_rectangulo(rec_1.topright, rec_2) or
        punto_en_rectangulo(rec_1.bottomleft, rec_2) or
        punto_en_rectangulo(rec_1.bottomright, rec_2) or
        punto_en_rectangulo(rec_2.topleft, rec_1) or
        punto_en_rectangulo(rec_2.topright, rec_1) or
        punto_en_rectangulo(rec_2.bottomleft, rec_1) or
        punto_en_rectangulo(rec_2.bottomright, rec_1)
    ):
        return True
    else:
        return False

def punto_en_rectangulo(punto, rect):
    x, y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom


def crear_bloque(left=0, top=0, ancho=50, alto=50, color=(255, 255, 255), dir=3, borde=0, radio=-1, speed_x=5, speed_y=5):
    rec = pygame.Rect(left, top, ancho, alto)
    return {"rect": rec, "color": color, "dir": dir, "borde": borde, "radio": radio, "speed_x": speed_x, "speed_y": speed_y}

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

BLOCK_WIDTH = 100
BLOCK_HEIGHT = 100
speed_x = 5
speed_y = 5 

# Creo el rectangulo
blocks = []

for i in range(2):
    blocks.append(crear_bloque(randint(0, width - BLOCK_WIDTH), randint(0, height - BLOCK_WIDTH), randint(20, BLOCK_WIDTH), randint(20, BLOCK_HEIGHT), color_aleatorio()))

# blocks = [
#     {"rect": pygame.Rect(randint(0, width - BLOCK_WIDTH), randint(0, height - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": color_random(colours), "dir": DL, "borde": 0, "radio": -1}, 
#     {"rect": pygame.Rect(randint(0, width - BLOCK_WIDTH), randint(0, height - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": color_aleatorio(), "dir": DL, "borde": 0, "radio": -1}, 
#     {"rect": pygame.Rect(randint(0, width - BLOCK_WIDTH), randint(0, height - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT), "color": color_random(colours), "dir": DL, "borde": 0, "radio": -1}, 
# ]
         

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
    for block in blocks:
        if block["rect"].right >= width:
            if block["dir"] == DR:
                block["dir"] = DL
            elif block["dir"] == UR:
                block["dir"] = UL
            # block["color"] = color_aleatorio()
            block["borde"] = randrange(20)
            block["speed_x"] = randint(1, 10)
        # Cuando choco con el lateral izquierdo
        elif block["rect"].left <= 0:
            if block["dir"] == DL:
                block["dir"] = DR
            elif block["dir"] == UL:
                block["dir"] = UR
            # block["color"] = color_aleatorio()
            block["radio"] = randrange(25)
            block["speed_x"] = randint(1, 10)
        # Cuando choco con la parte inferior
        elif block["rect"].bottom >= height:
            if block["dir"] == DR:
                block["dir"] = UR
            elif block["dir"] == DL:
                block["dir"] = UL
            # block["color"] = color_aleatorio()
            block["speed_y"] = randint(1, 10)
        # Cuando choco con la parte superior
        elif block["rect"].top <= 0:
            if block["dir"] == UR:
                block["dir"] = DR
            elif block["dir"] == UL:
                block["dir"] = DL
            # block["color"] = color_aleatorio()
            block["speed_y"] = randint(1, 10)
            
    # Movimiento del bloque de acuerdo a su direccion
    for block in blocks:
        if block["dir"] == DR:
            block["rect"].top += speed_y
            block["rect"].left += speed_x
        elif block["dir"] == DL:
            block["rect"].left -= speed_x
            block["rect"].top += speed_y
        elif block["dir"] == UL:
            block["rect"].left -= speed_x
            block["rect"].top -= speed_y
        elif block["dir"] == UR:
            block["rect"].left += speed_x
            block["rect"].top -= speed_y
    
    if detectar_colision(blocks[0]["rect"], blocks[1]["rect"]):
        print("COLISION")
        for block in blocks:
            block["color"] = color_aleatorio()
    # ---> Dibujar pantalla
    screen.fill(BLACK)
    for block in blocks:
        draw.rect(screen, block["color"], block["rect"], block["borde"], block["radio"])
    
    # ---> Actualizar pantalla, puede ser flip o update()
    pygame.display.flip()
            
pygame.quit()
sys.exit()
            