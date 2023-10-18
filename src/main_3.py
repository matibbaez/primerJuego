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

BLOCK_WIDTH = 50
BLOCK_HEIGHT = 50
speed_x = 5
speed_y = 5 
size_coin = 30
contador = 0

# Fuente
fuente = pygame.font.SysFont(None, 48)

texto = fuente.render(f"Coins: {contador}", True, CUSTOM, BLACK)
rect_texto = texto.get_rect()
rect_texto.midtop = (width // 2, 30)   

# Creo el rectangulo
block = crear_bloque(randint(0, width - BLOCK_WIDTH), randint(0, height - BLOCK_WIDTH), BLOCK_WIDTH, BLOCK_HEIGHT, color_aleatorio())

# Crear lista de coins
coins = []
for i in range(25):
    coins.append(crear_bloque(randint(0, width - size_coin), randint(0, height - size_coin), size_coin, size_coin, YELLOW, radio = size_coin // 2))

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
    if block["rect"].right >= width:
        if block["dir"] == DR:
            block["dir"] = DL
        elif block["dir"] == UR:
            block["dir"] = UL
        # block["color"] = color_aleatorio()
        # block["borde"] = randrange(20)
        # block["speed_x"] = randint(1, 10)
    # Cuando choco con el lateral izquierdo
    elif block["rect"].left <= 0:
        if block["dir"] == DL:
            block["dir"] = DR
        elif block["dir"] == UL:
            block["dir"] = UR
        # block["color"] = color_aleatorio()
        # block["radio"] = randrange(25)
        # block["speed_x"] = randint(1, 10)
    # Cuando choco con la parte inferior
    elif block["rect"].bottom >= height:
        if block["dir"] == DR:
            block["dir"] = UR
        elif block["dir"] == DL:
            block["dir"] = UL
        # block["color"] = color_aleatorio()
        # block["speed_y"] = randint(1, 10)
    # Cuando choco con la parte superior
    elif block["rect"].top <= 0:
        if block["dir"] == UR:
            block["dir"] = DR
        elif block["dir"] == UL:
            block["dir"] = DL
        # block["color"] = color_aleatorio()
        # block["speed_y"] = randint(1, 10)
            
    # Movimiento del bloque de acuerdo a su direccion
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
        
    for coin in coins[ : ]:
        if detectar_colision(coin["rect"], block["rect"]):
            coins.remove(coin)
            contador += 1
            texto = fuente.render(f"Coins: {contador}", True, CUSTOM, BLACK)
            rect_texto = texto.get_rect()
            rect_texto.midtop = (width // 2, 30)        
    
    # ---> Dibujar pantalla
    screen.fill(BLACK)
    
    for coin in coins:
        draw.rect(screen, coin["color"], coin["rect"], coin["borde"], coin["radio"])
    
    draw.rect(screen, block["color"], block["rect"], block["borde"], block["radio"])
    
    screen.blit(texto, rect_texto)
    
    # ---> Actualizar pantalla, puede ser flip o update()
    pygame.display.flip()
            
pygame.quit()
sys.exit()
            